from nselib import capital_market

df = capital_market.equity_list()

print(
    df[
        df["SYMBOL"]
        .astype(str)
        .str.contains("ADLABS", case=False, na=False)
    ]
)

print(
    df[
        df["NAME OF COMPANY"]
        .astype(str)
        .str.contains("Adlabs", case=False, na=False)
    ]
)