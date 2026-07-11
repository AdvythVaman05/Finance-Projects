import streamlit as st

VALID_INTERVALS = {
    "1 Day": ["1m", "2m", "5m", "15m", "30m"],
    "5 Days": ["5m", "15m", "30m", "60m"],
    "1 Month": ["30m", "60m", "1d"],
    "3 Months": ["1d"],
    "6 Months": ["1d"],
    "1 Year": ["1d"],
    "2 Years": ["1d", "1wk"],
    "5 Years": ["1wk", "1mo"],
    "Max": ["1wk", "1mo"]
}


def render_sidebar():

    st.sidebar.header("Search")

    ticker = st.sidebar.text_input(
        "Stock Symbol",
        value="TCS.NS"
    )

    st.sidebar.divider()

    period = st.sidebar.selectbox(
        "History",
        list(VALID_INTERVALS.keys()),
        index=2          # 1 Month
    )

    interval = st.sidebar.selectbox(
        "Interval",
        VALID_INTERVALS[period]
    )

    st.sidebar.divider()

    st.sidebar.subheader("Indicators")

    ema = st.sidebar.checkbox("EMA")
    rsi = st.sidebar.checkbox("RSI")
    macd = st.sidebar.checkbox("MACD")
    bb = st.sidebar.checkbox("Bollinger Bands")

    return ticker, period, interval, ema, rsi, macd, bb