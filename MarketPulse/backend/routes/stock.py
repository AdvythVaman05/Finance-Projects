from fastapi import APIRouter, HTTPException

from services.market_service import MarketService

router = APIRouter(
    prefix="/stock",
    tags=["Stock"]
)

service = MarketService()


@router.get("")
def get_stock(
    ticker: str,
    period: str = "1mo",
    interval: str = "30m"
):

    data = service.get_history(
        ticker,
        period,
        interval
    )

    if data is None:

        raise HTTPException(
            status_code=404,
            detail="Ticker not found."
        )

    return {
        "ticker": ticker,
        "history": data
    }