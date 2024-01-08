from fastapi import APIRouter
from fastapi.responses import JSONResponse

from application.binance_data_application import BinanceDataApplication
from container.api_binance_data_container import ApiBinanceDataContainer
from tools.yaml_reader import YAMLReader
from tools.constants import Table, RelativePath
from typing import Optional

router = APIRouter(
    prefix="/historical",
    tags=["Historical Data"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_historical_data(start: Optional[int] = 1, end: Optional[int] = 50):
    container = ApiBinanceDataContainer(
        binance_api_settings=YAMLReader(RelativePath.BINANCE_API_SETTINGS),
        binance_data_application=BinanceDataApplication(),
    )

    binanceDataApp = container.build_binance_data_application(
        Table.HISTORICAL_DATA
    )
    df_total = binanceDataApp.find_all()
    df_segment = df_total[start-1:end]
    json_data = df_segment.to_dict(orient="records")
    return JSONResponse(
        content={
            "rows": f"{len(json_data)} of {len(df_total)}",
            "data": json_data
        },
        status_code=200
    )
