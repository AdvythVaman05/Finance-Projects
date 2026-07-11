import requests

BASE_URL = "http://127.0.0.1:8000"


class BackendAPI:

    def search(self, query: str):

        if len(query) < 2:
            return []

        response = requests.get(
            f"{BASE_URL}/search",
            params={"q": query},
            timeout=5
        )

        response.raise_for_status()

        return response.json()

    def get_stock(
        self,
        ticker,
        period,
        interval
    ):

        response = requests.get(
            f"{BASE_URL}/stock",
            params={
                "ticker": ticker,
                "period": period,
                "interval": interval
            },
            timeout=10
        )

        response.raise_for_status()

        return response.json()
    
    def get_company(
    self,
    ticker
    ):

        response = requests.get(
            f"{BASE_URL}/company",
            params={
                "ticker": ticker
            },
            timeout=10
        )

        response.raise_for_status()

        return response.json()