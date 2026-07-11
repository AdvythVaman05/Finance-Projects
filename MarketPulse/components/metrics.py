import streamlit as st


def render_metrics():

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    col1.metric("Price", "--")

    col2.metric("Change", "--")

    col3.metric("Open", "--")

    col4.metric("High", "--")

    col5.metric("Low", "--")

    col6.metric("Volume", "--")