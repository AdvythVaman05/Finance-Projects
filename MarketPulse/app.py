import streamlit as st

from components.sidebar import render_sidebar
from components.chart import render_chart
from components.metrics import render_metrics

st.set_page_config(
    page_title="MarketPulse",
    page_icon="📈",
    layout="wide"
)

st.title("📈 MarketPulse")
st.caption("Real-Time Stock Market Dashboard")

ticker, interval = render_sidebar()

render_chart()

render_metrics()