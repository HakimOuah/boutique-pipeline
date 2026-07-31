import csv

from dropilot.sources.mapped_file import map_source_file


def test_csv_source_can_be_mapped_without_guessing_schema(tmp_path):
    source = tmp_path / "source.csv"
    with source.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["title", "cost"])
        writer.writeheader()
        writer.writerow({"title": "Produit A", "cost": "42"})
    mapping = tmp_path / "mapping.yaml"
    mapping.write_text("constants:\n  source: vevor\nfields:\n  product_name: title\n  price_source: cost\n", encoding="utf-8")
    row = map_source_file(source, mapping)[0]
    assert row["source"] == "vevor"
    assert row["product_name"] == "Produit A"
    assert row["price_source"] == "42"

