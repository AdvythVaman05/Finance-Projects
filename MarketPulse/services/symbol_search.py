import pandas as pd
from rapidfuzz import process


class SymbolSearch:

    def __init__(self, dataframe):
        self.df = dataframe

    def search(self, query, limit=10):

        choices = self.df["display"]

        results = process.extract(
            query,
            choices,
            limit=limit
        )

        output = []

        for name, score, idx in results:

            output.append(
                {
                    "company": self.df.iloc[idx]["Company"],
                    "symbol": self.df.iloc[idx]["Symbol"],
                    "exchange": self.df.iloc[idx]["Exchange"],
                    "score": score
                }
            )

        return output