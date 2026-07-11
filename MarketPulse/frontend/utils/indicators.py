import pandas as pd


def ema(df: pd.DataFrame, period: int = 20):

    return (
        df["Close"]
        .ewm(
            span=period,
            adjust=False
        )
        .mean()
    )


def bollinger_bands(
    df: pd.DataFrame,
    period: int = 20,
    std_dev: int = 2
):

    sma = (
        df["Close"]
        .rolling(period)
        .mean()
    )

    std = (
        df["Close"]
        .rolling(period)
        .std()
    )

    upper = sma + std_dev * std
    lower = sma - std_dev * std

    return upper, lower


def rsi(
    df: pd.DataFrame,
    period: int = 14
):

    delta = df["Close"].diff()

    gain = delta.clip(lower=0)

    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()

    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss

    return 100 - (100 / (1 + rs))


def macd(df: pd.DataFrame):

    ema12 = df["Close"].ewm(
        span=12,
        adjust=False
    ).mean()

    ema26 = df["Close"].ewm(
        span=26,
        adjust=False
    ).mean()

    macd_line = ema12 - ema26

    signal = macd_line.ewm(
        span=9,
        adjust=False
    ).mean()

    histogram = macd_line - signal

    return macd_line, signal, histogram