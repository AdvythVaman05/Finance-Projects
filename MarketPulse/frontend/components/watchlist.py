import streamlit as st
from utils.watchlist_storage import (
    load_watchlist,
    save_watchlist
)


def render_watchlist(current_ticker):

    if "watchlist" not in st.session_state:
        st.session_state.watchlist = load_watchlist()

    st.sidebar.divider()
    st.sidebar.subheader("⭐ Watchlist")

    # Add current ticker
    if current_ticker:

        if st.sidebar.button("➕ Add Current Stock"):

            if current_ticker not in st.session_state.watchlist:

                st.session_state.watchlist.append(current_ticker)
                
                save_watchlist(st.session_state.watchlist)

    # Display watchlist
    for ticker in st.session_state.watchlist:

        col1, col2 = st.sidebar.columns([4, 1])

        with col1:

            if st.button(
                ticker,
                key=f"ticker_{ticker}"
            ):

                st.session_state.selected_ticker = ticker
                st.rerun()

        with col2:

            if st.button(
                "❌",
                key=f"remove_{ticker}"
            ):

                st.session_state.watchlist.remove(ticker)
                
                save_watchlist(st.session_state.watchlist)
                st.rerun()
            
            if st.sidebar.button("🗑 Clear Watchlist"):

                st.session_state.watchlist.clear()

                save_watchlist([])

                st.rerun()