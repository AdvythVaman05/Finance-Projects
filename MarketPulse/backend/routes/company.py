from fastapi import APIRouter

from services.market_service import MarketService


router = APIRouter(
    prefix="/company",
    tags=["Company"]
)

service = MarketService()


@router.get("")
def get_company(ticker: str):

    return service.get_info(ticker)