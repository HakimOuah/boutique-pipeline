from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from subprocess import CompletedProcess

import pytest


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "codex-chasse-clusters" / "tools" / "aliexpress_vps_gateway.py"
spec = importlib.util.spec_from_file_location("aliexpress_vps_gateway", MODULE_PATH)
assert spec is not None and spec.loader is not None
gateway = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gateway)


def test_build_ssh_command_has_no_remote_shell_command(tmp_path) -> None:
    command = gateway.build_ssh_command(
        "148.230.118.152", "root", tmp_path / "identity"
    )

    assert command[-1] == "root@148.230.118.152"
    assert "BatchMode=yes" in command
    assert "StrictHostKeyChecking=yes" in command


def test_build_ssh_command_rejects_shell_metacharacters(tmp_path) -> None:
    with pytest.raises(ValueError, match="Invalid VPS host"):
        gateway.build_ssh_command("148.230.118.152;id", "root", tmp_path / "key")


def test_call_gateway_sends_json_on_stdin_without_shell(tmp_path, monkeypatch) -> None:
    identity = tmp_path / "identity"
    identity.write_text("test")
    observed = {}

    def fake_run(command, **kwargs):
        observed["command"] = command
        observed["input"] = kwargs["input"]
        observed["shell"] = kwargs.get("shell")
        return CompletedProcess(command, 0, '{"ok":true}', "")

    monkeypatch.setattr(gateway.subprocess, "run", fake_run)

    response = gateway.call_gateway(
        {"action": "health"},
        host="148.230.118.152",
        user="root",
        identity=identity,
    )

    assert response == {"ok": True}
    assert json.loads(observed["input"]) == {"action": "health"}
    assert observed["shell"] is None
    assert observed["command"][-1] == "root@148.230.118.152"


def test_search_request_exposes_only_allowlisted_sort_modes() -> None:
    parser = gateway._parser()
    args = parser.parse_args(
        ["search", "wooden cat tree", "--sort-by", "price_desc"]
    )

    assert gateway._request_from_args(args) == {
        "action": "search",
        "query": "wooden cat tree",
        "limit": 10,
        "destination": "FR",
        "sort_by": "price_desc",
    }

    with pytest.raises(SystemExit):
        parser.parse_args(["search", "wooden cat tree", "--sort-by", "unsafe"])
