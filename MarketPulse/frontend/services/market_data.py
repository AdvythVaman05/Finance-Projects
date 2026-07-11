import pandas as pd

from services.backend_api import BackendAPI


class MarketDataService:

    def __init__(self):

        self.api = BackendAPI()

    def get_history(
        self,
        ticker,
        period,
        interval
    ):

        response = self.api.get_stock(
            ticker,
            period,
            interval
        )

        df = pd.DataFrame(
            response["history"]
        )

        df["Date"] = pd.to_datetime(
            df["Date"]
        )

        df.set_index(
            "Date",
            inplace=True
        )

        return df
    
    def get_company(
        self,
        ticker
    ):

        return self.api.get_company(ticker)