import streamlit as st
from streamlit_autorefresh import st_autorefresh
from datetime import datetime

from components.search import stock_search
from components.chart import render_chart
from components.metrics import render_metrics
from components.sidebar import render_sidebar
from components.company_card import render_company_card
from components.watchlist import render_watchlist
from services.market_data import MarketDataService
from utils.market_status import get_market_status

@st.cache_data(ttl=600)
def get_cached_company_info(ticker):

    service = MarketDataService()
    data = service.get_company(ticker)

    # Do not treat empty fallback data as valid company information
    if not data or not data.get("market_cap"):
        raise ValueError(
            f"Company information unavailable for {ticker}"
        )

    return data

st.set_page_config(
    page_title="MarketPulse",
    page_icon="📈",
    layout="wide"
)

st.title("📈 MarketPulse")
st.caption("Real-Time Stock Dashboard")

(
    period,
    interval,
    ema,
    rsi,
    macd,
    bb,
    live_mode,
    refresh_interval
) = render_sidebar()

# Enable auto-refresh only if Live Mode is ON
if live_mode:
    st_autorefresh(
        interval=refresh_interval * 1000,
        key="market_refresh"
    )

# Search Company
ticker = stock_search()

render_watchlist(ticker)

if ticker:
    st.info(get_market_status(ticker))

if ticker:

    st.success(f"Selected\n{ticker}")

    service = MarketDataService()

    try:
        company_info = get_cached_company_info(ticker)

    except Exception as e:
        company_info = None
        print(f"Company API error for {ticker}: {e}")


    if company_info:

        try:
            render_company_card(company_info)

        except Exception as e:
            st.warning(
                "Company information could not be displayed."
            )

            print(f"Company card rendering error: {e}")

    else:

        st.warning(
            "Company information is temporarily unavailable. "
            "Market data is still available."
        )

    try:

        with st.spinner("Fetching latest market data..."):

            df = service.get_history(
                ticker=ticker,
                period=period,
                interval=interval
            )

        render_chart(df, ticker, ema, rsi, macd, bb, interval)

        render_metrics(df)
        
        csv = df.to_csv(index=True).encode("utf-8")

        st.download_button(
            "📥 Download CSV",
            csv,
            file_name=f"{ticker}.csv",
            mime="text/csv"
)

        st.caption(
            f"Last Updated: {datetime.now().strftime('%H:%M:%S')}"
        )

    except Exception as e:

        st.error(str(e))

else:

    st.info("Search for a company to begin.")

st.divider()

st.caption(
    "MarketPulse v1.0 | Powered by Yahoo Finance | Built with FastAPI & Streamlit"
)