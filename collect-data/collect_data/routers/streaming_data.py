from fastapi import APIRouter
from fastapi.responses import JSONResponse

from application.binance_data_application import BinanceDataApplication
from container.api_binance_data_container import ApiBinanceDataContainer
from tools.yaml_reader import YAMLReader
from tools.constants import Binance, RelativePath


container = ApiBinanceDataContainer(
    binance_api_settings=YAMLReader(RelativePath.BINANCE_API_SETTINGS),
    binance_data_application=BinanceDataApplication(),
)

binanceDataApp = \
    container.build_binance_data_application(Binance.STREAMING_DATA)

router = APIRouter(
    prefix="/streaming",
    tags=["Streaming Data"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_streaming_data():
    df = binanceDataApp.find_all()
    json_data = df.to_dict(orient="records")
    return JSONResponse(content=json_data, status_code=200)
