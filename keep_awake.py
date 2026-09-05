#!/usr/bin/env python3
"""Empêche macOS de se mettre en veille en simulant un léger mouvement de souris."""

from __future__ import annotations

import argparse
import ctypes
import signal
import time


class CGPoint(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]


APPLICATION_SERVICES = ctypes.cdll.LoadLibrary(
    "/System/Library/Frameworks/ApplicationServices.framework/ApplicationServices"
)

APPLICATION_SERVICES.CGEventCreate.argtypes = [ctypes.c_void_p]
APPLICATION_SERVICES.CGEventCreate.restype = ctypes.c_void_p
APPLICATION_SERVICES.CGEventGetLocation.argtypes = [ctypes.c_void_p]
APPLICATION_SERVICES.CGEventGetLocation.restype = CGPoint
APPLICATION_SERVICES.CGEventCreateMouseEvent.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    CGPoint,
    ctypes.c_uint32,
]
APPLICATION_SERVICES.CGEventCreateMouseEvent.restype = ctypes.c_void_p
APPLICATION_SERVICES.CGEventPost.argtypes = [ctypes.c_uint32, ctypes.c_void_p]
APPLICATION_SERVICES.CFRelease.argtypes = [ctypes.c_void_p]

MOUSE_MOVED = 5
HID_EVENT_TAP = 0
NO_BUTTON = 0


def mouse_position() -> CGPoint:
    event = APPLICATION_SERVICES.CGEventCreate(None)
    if not event:
        raise RuntimeError("Impossible de lire la position de la souris.")
    try:
        return APPLICATION_SERVICES.CGEventGetLocation(event)
    finally:
        APPLICATION_SERVICES.CFRelease(event)


def move_mouse(point: CGPoint) -> None:
    event = APPLICATION_SERVICES.CGEventCreateMouseEvent(
        None, MOUSE_MOVED, point, NO_BUTTON
    )
    if not event:
        raise RuntimeError("Impossible de créer l'événement de souris.")
    try:
        APPLICATION_SERVICES.CGEventPost(HID_EVENT_TAP, event)
    finally:
        APPLICATION_SERVICES.CFRelease(event)


def nudge_mouse() -> None:
    original = mouse_position()
    move_mouse(CGPoint(original.x + 1, original.y))
    time.sleep(0.1)
    move_mouse(original)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Garde le Mac éveillé en bougeant légèrement la souris."
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=30.0,
        help="Secondes entre deux mouvements (30 par défaut).",
    )
    args = parser.parse_args()
    if args.interval <= 0:
        parser.error("--interval doit être supérieur à 0")
    return args


def main() -> None:
    args = parse_args()
    running = True

    def stop(_signum: int, _frame: object) -> None:
        nonlocal running
        running = False

    signal.signal(signal.SIGINT, stop)
    signal.signal(signal.SIGTERM, stop)

    print(
        f"Maintien éveillé actif (mouvement toutes les {args.interval:g} s). "
        "Appuyez sur Ctrl+C pour arrêter."
    )
    while running:
        nudge_mouse()
        deadline = time.monotonic() + args.interval
        while running and time.monotonic() < deadline:
            time.sleep(min(0.5, deadline - time.monotonic()))

    print("Maintien éveillé arrêté.")


if __name__ == "__main__":
    main()
