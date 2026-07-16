import yfinance as yf


PERIOD_MAP = {
    "1 Day": "1d",
    "5 Days": "5d",
    "1 Month": "1mo",
    "3 Months": "3mo",
    "6 Months": "6mo",
    "1 Year": "1y",
    "2 Years": "2y",
    "5 Years": "5y",
    "Max": "max"
}


INTRADAY_INTERVALS = {
    "1m",
    "2m",
    "5m",
    "15m",
    "30m",
    "60m",
    "90m",
    "1h"
}


class MarketService:

    def get_history(
        self,
        ticker: str,
        period: str,
        interval: str
    ):

        requested_period = PERIOD_MAP.get(
            period,
            period
        )

        # For a live 1-day intraday chart, fetch several
        # trading sessions instead of only today's session.
        #
        # This prevents the previous day's candles from
        # disappearing when a new trading day begins.
        if (
            requested_period == "1d"
            and interval in INTRADAY_INTERVALS
        ):
            download_period = "5d"

        else:
            download_period = requested_period

        df = yf.download(
            tickers=ticker,
            period=download_period,
            interval=interval,
            progress=False,
            auto_adjust=False,
            multi_level_index=False
        )

        if df is None or df.empty:
            return None

        df.reset_index(inplace=True)

        first_column = df.columns[0]

        df.rename(
            columns={
                first_column: "Date"
            },
            inplace=True
        )

        df["Date"] = df["Date"].astype(str)

        return df.to_dict(
            orient="records"
        )

    def get_info(
        self,
        ticker: str
    ):

        try:

            stock = yf.Ticker(ticker)

            info = stock.info or {}

            dividend = info.get(
                "dividendYield"
            )

            if dividend is not None:
                dividend *= 100

            return {

                "company": (
                    info.get("longName")
                    or info.get("shortName")
                    or ticker
                ),

                "symbol": ticker,

                "sector": info.get("sector"),

                "industry": info.get("industry"),

                "exchange": info.get("exchange"),

                "currency": info.get("currency"),

                "market_cap": info.get("marketCap"),

                "previous_close": info.get(
                    "previousClose"
                ),

                "open": info.get("open"),

                "day_high": info.get("dayHigh"),

                "day_low": info.get("dayLow"),

                "fifty_two_week_high": info.get(
                    "fiftyTwoWeekHigh"
                ),

                "fifty_two_week_low": info.get(
                    "fiftyTwoWeekLow"
                ),

                "pe": info.get("trailingPE"),

                "dividend": dividend
            }

        except Exception as e:

            print(
                f"Yahoo Finance company info failed "
                f"for {ticker}: {e}"
            )

            return {

                "company": ticker,

                "symbol": ticker,

                "sector": None,

                "industry": None,

                "exchange": None,

                "currency": None,

                "market_cap": None,

                "previous_close": None,

                "open": None,

                "day_high": None,

                "day_low": None,

                "fifty_two_week_high": None,

                "fifty_two_week_low": None,

                "pe": None,

                "dividend": None
            }