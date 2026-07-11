import streamlit as st

def render_sidebar():

    st.sidebar.header("Search")

    ticker = st.sidebar.text_input(
        "Stock Symbol",
        value="TCS.NS"
    )

    interval = st.sidebar.selectbox(
        "Interval",
        [
            "1m",
            "2m",
            "5m",
            "15m",
            "30m",
            "60m",
            "1d"
        ]
    )

    st.sidebar.divider()

    st.sidebar.subheader("Indicators")

    st.sidebar.checkbox("EMA", value=True)

    st.sidebar.checkbox("RSI")

    st.sidebar.checkbox("MACD")

    st.sidebar.checkbox("Bollinger Bands")

    return ticker, interval