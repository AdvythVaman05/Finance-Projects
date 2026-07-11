from fastapi import FastAPI

from routes.search import router as search_router
from routes.stock import router as stock_router
from routes.company import router as company_router

app = FastAPI(
    title="MarketPulse Backend",
    version="1.0"
)

app.include_router(search_router)
app.include_router(stock_router)
app.include_router(company_router)


@app.get("/")
def root():
    return {"message": "Backend Running"}