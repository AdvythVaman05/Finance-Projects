import streamlit as st

from services.backend_api import BackendAPI

api = BackendAPI()


def stock_search():

    if "selected_ticker" not in st.session_state:
        st.session_state.selected_ticker = None

    query = st.text_input(
    "🔍 Search Company",
    key="search_box",
    placeholder="Search..."
)

    if query:

        results = api.search(query)

        if not results:

            st.warning("No matching company found.")
            return st.session_state.selected_ticker

        options = {
            f"{item['company']} ({item['symbol']})": item["symbol"]
            for item in results
        }

        selected = st.selectbox(
            "Select Company",
            list(options.keys())
        )

        st.session_state.selected_ticker = options[selected]

    return st.session_state.selected_ticker