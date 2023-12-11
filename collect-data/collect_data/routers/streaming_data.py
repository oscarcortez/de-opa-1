from fastapi import APIRouter
from fastapi.responses import JSONResponse

from application.binance_data_application import BinanceDataApplication
from container.api_binance_data_container import ApiBinanceDataContainer
from tools.yaml_reader import YAMLReader
from tools.constants import Table, RelativePath


router = APIRouter(
    prefix="/streaming",
    tags=["Streaming Data"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_streaming_data():
    container = ApiBinanceDataContainer(
        binance_api_settings=YAMLReader(RelativePath.BINANCE_API_SETTINGS),
        binance_data_application=BinanceDataApplication())
    binanceDataApp = \
        container.build_binance_data_application(Table.STREAMING_DATA)
    df = binanceDataApp.find_all()
    json_data = df.to_dict(orient="records")
    return JSONResponse(content={"rows": len(json_data), "data": json_data},
                        status_code=200)
