import json

from dropilot.sources.bigbuy import BigBuyClient, fetch_bigbuy_candidates


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return None

    def read(self):
        return json.dumps(self.payload).encode("utf-8")


def test_bigbuy_catalog_and_information_are_joined():
    def opener(request, timeout):
        if "productsinformation" in request.full_url:
            return FakeResponse([{"id": 10, "name": "Produit test", "url": "produit-test_10"}])
        return FakeResponse(
            [
                {
                    "id": 10,
                    "sku": "SKU10",
                    "active": 1,
                    "wholesalePrice": 100,
                    "inShopsPrice": 450,
                    "retailPrice": 150,
                }
            ]
        )

    client = BigBuyClient(api_key="test", opener=opener)
    candidate = fetch_bigbuy_candidates(client, 42)[0]
    assert candidate.product_name == "Produit test"
    assert candidate.price_source == 100
    assert candidate.price_sell == 450
    assert candidate.metadata["sku"] == "SKU10"


def test_bigbuy_requires_a_key(monkeypatch):
    monkeypatch.delenv("BIGBUY_API_KEY", raising=False)
    try:
        BigBuyClient(api_key="")
        assert False, "une clé est obligatoire"
    except ValueError as error:
        assert "BIGBUY_API_KEY" in str(error)
