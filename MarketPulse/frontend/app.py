import streamlit as st

from MarketPulse.frontend.components.chart import render_chart
from MarketPulse.frontend.components.metrics import render_metrics
from MarketPulse.frontend.components.sidebar import render_sidebar
from MarketPulse.frontend.services.market_data import MarketDataService

st.set_page_config(
    page_title="MarketPulse",
    page_icon="📈",
    layout="wide"
)

st.title("📈 MarketPulse")

ticker, period, interval, ema, rsi, macd, bb = render_sidebar()

service = MarketDataService()

try:
    df = service.get_history(
        ticker=ticker,
        period=period,
        interval=interval
    )

    render_chart(df)
    render_metrics(df)

except Exception as e:
    st.error(str(e))