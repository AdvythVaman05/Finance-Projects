import streamlit as st
import plotly.graph_objects as go
import pandas as pd

from utils.indicators import (
    ema,
    bollinger_bands,
    rsi,
    macd
)


INTRADAY_INTERVALS = {
    "1m",
    "2m",
    "5m",
    "15m",
    "30m",
    "60m",
    "90m",
    "1h"
}


def render_chart(
    df,
    ticker,
    ema_enabled,
    rsi_enabled,
    macd_enabled,
    bb_enabled,
    interval
):

    # Make a copy so the original dataframe
    # is not modified.
    df = df.copy()

    # Ensure chronological order
    df = df.sort_index()

    # Remove duplicate timestamps if present
    df = df[
        ~df.index.duplicated(
            keep="last"
        )
    ]

    # ==========================================
    # CREATE CONTINUOUS TRADING-TIME X AXIS
    # ==========================================

    is_intraday = (
        interval in INTRADAY_INTERVALS
    )

    if is_intraday:

        # Every candle receives a sequential position:
        #
        # 0, 1, 2, 3, 4 ...
        #
        # Therefore:
        #
        # Jul 15 15:29 -> candle 374
        # Jul 16 09:15 -> candle 375
        #
        # No overnight gap can exist.

        x_values = list(
            range(len(df))
        )

        # Real timestamps are kept for hover
        datetime_values = (
            pd.to_datetime(df.index)
            .strftime(
                "%d %b %Y<br>%H:%M"
            )
            .tolist()
        )

    else:

        # Normal datetime axis for
        # daily/weekly/long-term charts
        x_values = df.index

        datetime_values = (
            pd.to_datetime(df.index)
            .strftime(
                "%d %b %Y"
            )
            .tolist()
        )

    # ==========================================
    # X AXIS LABELS
    # ==========================================

    if is_intraday:

        # Show around 8 labels across the chart
        tick_count = 8

        step = max(
            1,
            len(df) // tick_count
        )

        tick_positions = list(
            range(
                0,
                len(df),
                step
            )
        )

        tick_labels = [

            pd.to_datetime(
                df.index[position]
            ).strftime(
                "%H:%M<br>%d %b"
            )

            for position
            in tick_positions
        ]

    else:

        tick_positions = None
        tick_labels = None

    # ==========================================
    # COMMON X AXIS CONFIGURATION
    # ==========================================

    def configure_xaxis(figure):

        if is_intraday:

            figure.update_xaxes(

                type="linear",

                tickmode="array",

                tickvals=tick_positions,

                ticktext=tick_labels,

                range=[
                    -1,
                    len(df)
                ],

                minallowed=-1,

                maxallowed=len(df)
            )

    # ==========================================
    # PRICE CHART
    # ==========================================

    fig = go.Figure()

    fig.add_trace(

        go.Candlestick(

            x=x_values,

            open=df["Open"],

            high=df["High"],

            low=df["Low"],

            close=df["Close"],

            name="Price",

            customdata=datetime_values,

            hovertext=datetime_values,

            hoverinfo="text+x+y"
        )
    )

    # ==========================================
    # EMA
    # ==========================================

    if ema_enabled:

        ema_values = ema(df)

        fig.add_trace(

            go.Scatter(

                x=x_values,

                y=ema_values,

                mode="lines",

                name="EMA 20",

                customdata=datetime_values,

                hovertemplate=(
                    "%{customdata}"
                    "<br>EMA 20: %{y:.2f}"
                    "<extra></extra>"
                ),

                line=dict(
                    color="orange",
                    width=2
                )
            )
        )

    # ==========================================
    # BOLLINGER BANDS
    # ==========================================

    if bb_enabled:

        upper, lower = (
            bollinger_bands(df)
        )

        fig.add_trace(

            go.Scatter(

                x=x_values,

                y=upper,

                mode="lines",

                name="Upper Band",

                customdata=datetime_values,

                hovertemplate=(
                    "%{customdata}"
                    "<br>Upper Band: %{y:.2f}"
                    "<extra></extra>"
                ),

                line=dict(
                    color="cyan",
                    width=1
                )
            )
        )

        fig.add_trace(

            go.Scatter(

                x=x_values,

                y=lower,

                mode="lines",

                name="Lower Band",

                customdata=datetime_values,

                hovertemplate=(
                    "%{customdata}"
                    "<br>Lower Band: %{y:.2f}"
                    "<extra></extra>"
                ),

                line=dict(
                    color="cyan",
                    width=1
                )
            )
        )

    fig.update_layout(

        title=f"{ticker} Candlestick Chart",

        template="plotly_dark",

        height=650,

        hovermode="x unified",

        xaxis_rangeslider_visible=False,

        legend=dict(

            orientation="h",

            yanchor="top",

            y=1.12,

            xanchor="center",

            x=0.5,

            bgcolor="rgba(0,0,0,0)"
        ),

        margin=dict(
            l=20,
            r=20,
            t=90,
            b=20
        )
    )

    configure_xaxis(fig)

    fig.update_yaxes(
        title="Price"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ==========================================
    # VOLUME CHART
    # ==========================================

    volume_colors = [

        "green"
        if close >= open_price
        else "red"

        for open_price, close
        in zip(
            df["Open"],
            df["Close"]
        )
    ]

    volume_fig = go.Figure()

    volume_fig.add_trace(

        go.Bar(

            x=x_values,

            y=df["Volume"],

            marker_color=volume_colors,

            customdata=datetime_values,

            hovertemplate=(
                "%{customdata}"
                "<br>Volume: %{y:,.0f} shares"
                "<extra></extra>"
            ),

            name="Volume"
        )
    )

    volume_fig.update_layout(

        title="Trading Volume",

        template="plotly_dark",

        height=250,

        showlegend=False,

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        )
    )

    configure_xaxis(
        volume_fig
    )

    volume_fig.update_yaxes(
        title="Volume (Shares)"
    )

    st.plotly_chart(
        volume_fig,
        use_container_width=True
    )

    # ==========================================
    # RSI
    # ==========================================

    if rsi_enabled:

        rsi_values = rsi(df)

        rsi_fig = go.Figure()

        rsi_fig.add_trace(

            go.Scatter(

                x=x_values,

                y=rsi_values,

                mode="lines",

                customdata=datetime_values,

                hovertemplate=(
                    "%{customdata}"
                    "<br>RSI: %{y:.2f}"
                    "<extra></extra>"
                ),

                line=dict(
                    color="yellow",
                    width=2
                ),

                name="RSI"
            )
        )

        rsi_fig.add_hline(

            y=70,

            line_dash="dash",

            line_color="red"
        )

        rsi_fig.add_hline(

            y=30,

            line_dash="dash",

            line_color="green"
        )

        rsi_fig.update_layout(

            title=(
                "Relative Strength "
                "Index (RSI)"
            ),

            template="plotly_dark",

            height=250,

            margin=dict(
                l=20,
                r=20,
                t=50,
                b=20
            )
        )

        configure_xaxis(
            rsi_fig
        )

        rsi_fig.update_yaxes(

            title="RSI",

            range=[
                0,
                100
            ]
        )

        st.plotly_chart(

            rsi_fig,

            use_container_width=True
        )

    # ==========================================
    # MACD
    # ==========================================

    if macd_enabled:

        (
            macd_line,
            signal_line,
            histogram
        ) = macd(df)

        histogram_colors = [

            "green"
            if value >= 0
            else "red"

            for value
            in histogram
        ]

        macd_fig = go.Figure()

        macd_fig.add_trace(

            go.Bar(

                x=x_values,

                y=histogram,

                marker_color=(
                    histogram_colors
                ),

                customdata=(
                    datetime_values
                ),

                hovertemplate=(
                    "%{customdata}"
                    "<br>Histogram: %{y:.2f}"
                    "<extra></extra>"
                ),

                name="Histogram"
            )
        )

        macd_fig.add_trace(

            go.Scatter(

                x=x_values,

                y=macd_line,

                mode="lines",

                customdata=(
                    datetime_values
                ),

                hovertemplate=(
                    "%{customdata}"
                    "<br>MACD: %{y:.2f}"
                    "<extra></extra>"
                ),

                line=dict(
                    color="cyan",
                    width=2
                ),

                name="MACD"
            )
        )

        macd_fig.add_trace(

            go.Scatter(

                x=x_values,

                y=signal_line,

                mode="lines",

                customdata=(
                    datetime_values
                ),

                hovertemplate=(
                    "%{customdata}"
                    "<br>Signal: %{y:.2f}"
                    "<extra></extra>"
                ),

                line=dict(
                    color="orange",
                    width=2
                ),

                name="Signal"
            )
        )

        macd_fig.update_layout(

            title="MACD",

            template="plotly_dark",

            height=300,

            margin=dict(
                l=20,
                r=20,
                t=50,
                b=20
            )
        )

        configure_xaxis(
            macd_fig
        )

        macd_fig.update_yaxes(
            title="MACD"
        )

        st.plotly_chart(

            macd_fig,

            use_container_width=True
        )