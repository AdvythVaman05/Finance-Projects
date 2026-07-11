from pathlib import Path

import pandas as pd


class SearchService:

    def __init__(self):

        path = (
            Path(__file__).parent.parent
            / "data"
            / "symbols.csv"
        )

        self.df = pd.read_csv(path)

        self.df["company_lower"] = (
            self.df["company"]
            .str.lower()
        )

        self.df["symbol_lower"] = (
            self.df["symbol"]
            .str.lower()
        )

    def search(
        self,
        query: str,
        limit: int = 10
    ):

        if len(query) < 2:
            return []

        query = query.lower()

        df = self.df.copy()

        df["score"] = 0

        # Exact symbol match
        df.loc[
            df["symbol_lower"] == query,
            "score"
        ] += 100

        # Symbol starts with query
        df.loc[
            df["symbol_lower"].str.startswith(query),
            "score"
        ] += 80

        # Company starts with query
        df.loc[
            df["company_lower"].str.startswith(query),
            "score"
        ] += 60

        # Company contains query
        df.loc[
            df["company_lower"].str.contains(query),
            "score"
        ] += 40

        # Symbol contains query
        df.loc[
            df["symbol_lower"].str.contains(query),
            "score"
        ] += 20

        results = (
            df[df["score"] > 0]
            .sort_values(
                ["score", "company"],
                ascending=[False, True]
            )
            .head(limit)
        )

        return results[
            ["symbol", "company", "exchange"]
        ].to_dict(
            orient="records"
        )