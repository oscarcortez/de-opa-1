from application.binance_data_application import BinanceDataApplication
from tools.data_yaml_generator import DataYamlGenerator
from tools.constants import RelativePath
from api_client.binance_api_client import BinanceApiClient
from container.binance_data_container import BinanceDataContainer
import sys


if __name__ == "__main__":

    binance_api_settings = DataYamlGenerator(yaml_file= RelativePath.BINANCE_API_SETTINGS)
    binance_api_client = BinanceApiClient()
    binance_data_application = BinanceDataApplication()    

    container = BinanceDataContainer(        
        binance_api_settings= binance_api_settings,
        binance_api_client= binance_api_client,
        binance_data_application= binance_data_application,
        command_arguments=sys.argv
    )

    container.execute()