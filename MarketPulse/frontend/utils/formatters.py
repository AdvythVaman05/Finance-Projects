def format_market_cap(value):

    if value is None:
        return "-"

    value = float(value)

    if value >= 1_000_000_000_000:
        return f"₹{value / 1_000_000_000_000:.2f}T"

    if value >= 1_000_000_000:
        return f"₹{value / 1_000_000_000:.2f}B"

    if value >= 1_000_000:
        return f"₹{value / 1_000_000:.2f}M"

    return f"₹{value:,.0f}"


def format_price(value):

    if value is None:
        return "-"

    return f"₹{value:.2f}"


def format_percentage(value):

    if value is None:
        return "-"

    return f"{value:.2f}%"