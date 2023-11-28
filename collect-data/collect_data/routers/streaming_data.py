from fastapi import APIRouter
# from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from application.binance_data_application import BinanceDataApplication

router = APIRouter(
    prefix="/streaming",
    tags=["Streaming Data"],
    responses={404: {"description": "Not found"}},
)


binanceDataApp = BinanceDataApplication(
    destination_source="BinanceDataPostgresRepository",
    table_name="binance_streaming_data",
)
binanceDataApp.set_binance_data_repository()


@router.get("/")
def get_streaming_data():
    df = binanceDataApp.find_all()
    json_data = df.to_dict(orient='records')
    return JSONResponse(content=json_data, status_code=200)
