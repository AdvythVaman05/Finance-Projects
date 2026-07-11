import streamlit as st


def render_metrics(data):

    latest = data.iloc[-1]
    previous = data.iloc[-2]

    change = latest["Close"] - previous["Close"]

    percent = (change / previous["Close"]) * 100

    c1, c2, c3, c4, c5, c6 = st.columns(6)

    c1.metric(
        "Price",
        f"{latest['Close']:.2f}"
    )

    c2.metric(
        "Change",
        f"{change:.2f}",
        f"{percent:.2f}%"
    )

    c3.metric(
        "Open",
        f"{latest['Open']:.2f}"
    )

    c4.metric(
        "High",
        f"{latest['High']:.2f}"
    )

    c5.metric(
        "Low",
        f"{latest['Low']:.2f}"
    )

    c6.metric(
        "Volume",
        f"{int(latest['Volume']):,}"
    )