import os
import requests
import streamlit as st
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def get_backend_url():

    if "BACKEND_URL" in st.secrets:
        return st.secrets["BACKEND_URL"]

    return os.getenv(
        "BACKEND_URL",
        "http://127.0.0.1:8000"
    )


BASE_URL = get_backend_url().rstrip("/")


retry_strategy = Retry(
    total=3,
    connect=3,
    read=3,
    backoff_factor=1,
    status_forcelist=[
        429,
        500,
        502,
        503,
        504
    ],
    allowed_methods=["GET"]
)

adapter = HTTPAdapter(
    max_retries=retry_strategy
)

session = requests.Session()

session.mount(
    "https://",
    adapter
)

session.mount(
    "http://",
    adapter
)

class BackendAPI:

    def search(self, query: str):

        if len(query) < 2:
            return []

        response = session.get(
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

        response = session.get(
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

        response = session.get(
            f"{BASE_URL}/company",
            params={
                "ticker": ticker
            },
            timeout=10
        )

        response.raise_for_status()

        return response.json()