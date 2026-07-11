from fastapi import FastAPI

from routes.search import router as search_router
from routes.stock import router as stock_router
from routes.symbols import router as symbols_router

app = FastAPI(
    title="MarketPulse Backend",
    version="1.0.0"
)

app.include_router(search_router)
app.include_router(stock_router)
app.include_router(symbols_router)


@app.get("/")
def root():
    return {
        "message": "MarketPulse Backend Running"
    }