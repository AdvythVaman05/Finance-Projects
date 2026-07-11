from fastapi import APIRouter, HTTPException

from services.market_service import MarketService

router = APIRouter(
    prefix="/company",
    tags=["Company"]
)

service = MarketService()


@router.get("")
def get_company(ticker: str):

    data = service.get_info(ticker)

    if data is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found."
        )

    if "error" in data:
        raise HTTPException(
            status_code=500,
            detail=data["error"]
        )

    return data