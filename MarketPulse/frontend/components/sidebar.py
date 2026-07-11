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

    st.sidebar.header("Chart Settings")

    period = st.sidebar.selectbox(
        "History",
        list(VALID_INTERVALS.keys()),
        index=2
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

    st.sidebar.divider()

    st.sidebar.subheader("Live Updates")

    live_mode = st.sidebar.toggle(
        "Enable Live Updates",
        value=False
    )

    refresh_interval = st.sidebar.selectbox(
        "Refresh Every (seconds)",
        [5, 10, 15, 30, 60],
        index=0,
        disabled=not live_mode
    )

    return (
        period,
        interval,
        ema,
        rsi,
        macd,
        bb,
        live_mode,
        refresh_interval
    )