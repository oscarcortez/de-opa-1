from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routers.streaming_data import router as StreamingRouter
from routers.historical_data import router as HistoricalRouter
from routers.historical_data_raw import router as HistoricalRouterRaw
from routers.streaming_data_raw import router as StreamingRouterRaw

api = FastAPI()
api.title = "Kryptobot"
api.description = "Kriptobot API"
api.version = "1.0.0"

api.include_router(StreamingRouter)
api.include_router(HistoricalRouter)
api.include_router(HistoricalRouterRaw)
api.include_router(StreamingRouterRaw)


@api.get("/", tags=["home"])
def default():
    return HTMLResponse(
        content="<h1>API is running from /api</h1>",
        status_code=200)
