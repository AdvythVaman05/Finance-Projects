import streamlit as st
import plotly.graph_objects as go

from utils.indicators import (
    ema,
    bollinger_bands,
    rsi,
    macd
)


def render_chart(
    df,
    ticker,
    ema_enabled,
    rsi_enabled,
    macd_enabled,
    bb_enabled,
    interval
):

    # ==========================
    # MARKET HOURS CONFIGURATION
    # ==========================

    intraday_intervals = {
        "1m",
        "2m",
        "5m",
        "15m",
        "30m",
        "60m",
        "90m",
        "1h"
    }

    rangebreaks = []

    # NSE trading hours:
    # 09:15 AM -> 03:30 PM
    if ticker.endswith(".NS") and interval in intraday_intervals:

        rangebreaks = [
            # Remove weekends
            dict(
                bounds=["sat", "mon"]
            ),

            # Remove overnight/non-trading hours
            dict(
                bounds=[15.5, 9.25],
                pattern="hour"
            )
        ]

    # Actual available data boundaries
    x_min = df.index.min()
    x_max = df.index.max()

    # ==========================
    # PRICE CHART
    # ==========================

    fig = go.Figure()

    fig.add_trace(
        go.Candlestick(
            x=df.index,
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            name="Price"
        )
    )

    # EMA
    if ema_enabled:

        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=ema(df),
                mode="lines",
                name="EMA 20",
                line=dict(
                    color="orange",
                    width=2
                )
            )
        )

    # Bollinger Bands
    if bb_enabled:

        upper, lower = bollinger_bands(df)

        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=upper,
                mode="lines",
                name="Upper Band",
                line=dict(
                    color="cyan",
                    width=1
                )
            )
        )

        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=lower,
                mode="lines",
                name="Lower Band",
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

    fig.update_xaxes(
        rangebreaks=rangebreaks,
        range=[x_min, x_max],
        minallowed=x_min,
        maxallowed=x_max
    )

    fig.update_yaxes(
        title="Price"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ==========================
    # VOLUME CHART
    # ==========================

    volume_colors = [
        "green" if c >= o else "red"
        for o, c in zip(
            df["Open"],
            df["Close"]
        )
    ]

    volume_fig = go.Figure()

    volume_fig.add_trace(
        go.Bar(
            x=df.index,
            y=df["Volume"],
            marker_color=volume_colors,
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

    volume_fig.update_xaxes(
        rangebreaks=rangebreaks,
        range=[x_min, x_max],
        minallowed=x_min,
        maxallowed=x_max
    )

    volume_fig.update_yaxes(
        title="Volume (Shares)"
    )

    st.plotly_chart(
        volume_fig,
        use_container_width=True
    )

    # ==========================
    # RSI
    # ==========================

    if rsi_enabled:

        rsi_values = rsi(df)

        rsi_fig = go.Figure()

        rsi_fig.add_trace(
            go.Scatter(
                x=df.index,
                y=rsi_values,
                mode="lines",
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
            title="Relative Strength Index (RSI)",
            template="plotly_dark",
            height=250,
            margin=dict(
                l=20,
                r=20,
                t=50,
                b=20
            )
        )

        rsi_fig.update_xaxes(
            rangebreaks=rangebreaks,
            range=[x_min, x_max],
            minallowed=x_min,
            maxallowed=x_max
        )

        rsi_fig.update_yaxes(
            title="RSI",
            range=[0, 100]
        )

        st.plotly_chart(
            rsi_fig,
            use_container_width=True
        )

    # ==========================
    # MACD
    # ==========================

    if macd_enabled:

        macd_line, signal_line, histogram = macd(df)

        histogram_colors = [
            "green" if value >= 0 else "red"
            for value in histogram
        ]

        macd_fig = go.Figure()

        macd_fig.add_trace(
            go.Bar(
                x=df.index,
                y=histogram,
                marker_color=histogram_colors,
                name="Histogram"
            )
        )

        macd_fig.add_trace(
            go.Scatter(
                x=df.index,
                y=macd_line,
                mode="lines",
                line=dict(
                    color="cyan",
                    width=2
                ),
                name="MACD"
            )
        )

        macd_fig.add_trace(
            go.Scatter(
                x=df.index,
                y=signal_line,
                mode="lines",
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

        macd_fig.update_xaxes(
            rangebreaks=rangebreaks,
            range=[x_min, x_max],
            minallowed=x_min,
            maxallowed=x_max
        )

        macd_fig.update_yaxes(
            title="MACD"
        )

        st.plotly_chart(
            macd_fig,
            use_container_width=True
        )