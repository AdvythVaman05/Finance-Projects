from datetime import datetime
from zoneinfo import ZoneInfo


def get_market_status(ticker):

    now_ist = datetime.now(ZoneInfo("Asia/Kolkata"))
    now_us = datetime.now(ZoneInfo("America/New_York"))

    if ticker.endswith(".NS"):

        if now_ist.weekday() >= 5:
            return "🔴 NSE Closed"

        current = now_ist.time()

        if current >= datetime.strptime("09:15", "%H:%M").time() and \
           current <= datetime.strptime("15:30", "%H:%M").time():

            return "🟢 NSE Open"

        return "🔴 NSE Closed"

    else:

        if now_us.weekday() >= 5:
            return "🔴 US Market Closed"

        current = now_us.time()

        if current >= datetime.strptime("09:30", "%H:%M").time() and \
           current <= datetime.strptime("16:00", "%H:%M").time():

            return "🟢 US Market Open"

        return "🔴 US Market Closed"