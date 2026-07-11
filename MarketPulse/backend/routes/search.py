from fastapi import APIRouter

from services.search_service import SearchService

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)

service = SearchService()


@router.get("")
def search_stock(q: str):

    return service.search(q)