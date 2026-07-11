from nselib import capital_market

df = capital_market.equity_list()

print(df.head())

print("\n")

print(df.columns)

print("\n")

print(df.shape)