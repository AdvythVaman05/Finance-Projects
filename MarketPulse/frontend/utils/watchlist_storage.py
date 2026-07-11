import json
from pathlib import Path

WATCHLIST_FILE = (
    Path(__file__).parent.parent
    / "data"
    / "watchlist.json"
)


def load_watchlist():

    if not WATCHLIST_FILE.exists():
        return []

    with open(
        WATCHLIST_FILE,
        "r"
    ) as f:

        return json.load(f)


def save_watchlist(watchlist):

    with open(
        WATCHLIST_FILE,
        "w"
    ) as f:

        json.dump(
            watchlist,
            f,
            indent=4
        )