import streamlit as st
import plotly.graph_objects as go


def render_chart():

    fig = go.Figure()

    fig.update_layout(
        height=600,
        template="plotly_dark",
        title="Candlestick Chart"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )