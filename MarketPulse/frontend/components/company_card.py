import streamlit as st

from utils.formatters import (
    format_market_cap,
    format_price,
    format_percentage
)


def render_company_card(info):

    if not info:
        return

    st.subheader(info.get("company", "Unknown Company"))

    st.caption(
        f"{info.get('symbol', '-')} • {info.get('exchange', '-')}"
    )

    sector = info.get("sector")
    industry = info.get("industry")

    if sector or industry:

        st.write(
            f"**Sector:** {sector or '-'} &nbsp;&nbsp;&nbsp; "
            f"**Industry:** {industry or '-'}"
        )

    st.divider()

    col1, col2, col3 = st.columns(3)

    # -------------------------
    # Column 1
    # -------------------------

    with col1:

        st.metric(
            "Market Cap",
            format_market_cap(
                info.get("market_cap")
            )
        )

        st.metric(
            "Previous Close",
            format_price(
                info.get("previous_close")
            )
        )

        st.metric(
            "Open",
            format_price(
                info.get("open")
            )
        )

    # -------------------------
    # Column 2
    # -------------------------

    with col2:

        st.metric(
            "Day High",
            format_price(
                info.get("day_high")
            )
        )

        st.metric(
            "Day Low",
            format_price(
                info.get("day_low")
            )
        )

        pe = info.get("pe")

        st.metric(
            "P/E Ratio",
            f"{pe:.2f}" if pe is not None else "-"
        )

    # -------------------------
    # Column 3
    # -------------------------

    with col3:

        st.metric(
            "52 Week High",
            format_price(
                info.get("fifty_two_week_high")
            )
        )

        st.metric(
            "52 Week Low",
            format_price(
                info.get("fifty_two_week_low")
            )
        )

        st.metric(
            "Dividend Yield",
            format_percentage(
                info.get("dividend")
            )
        )

    st.divider()