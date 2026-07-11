from pathlib import Path

import pandas as pd
from nselib import capital_market


def build_nse_database():

    print("Downloading NSE equity list...")

    df = capital_market.equity_list()

    symbols = (
        df[["SYMBOL", "NAME OF COMPANY"]]
        .copy()
        .rename(
            columns={
                "SYMBOL": "symbol",
                "NAME OF COMPANY": "company"
            }
        )
    )

    symbols["symbol"] = symbols["symbol"] + ".NS"
    symbols["exchange"] = "NSE"

    symbols = symbols.sort_values("company")
    symbols = symbols.drop_duplicates(subset=["symbol"])

    output = Path(__file__).parent.parent / "data" / "symbols.csv"

    symbols.to_csv(
        output,
        index=False
    )

    print(f"Saved {len(symbols)} symbols.")
    print(output)


if __name__ == "__main__":
    build_nse_database()