from application.binance_data_application import BinanceDataApplication
from config.data_yaml_generator import DataYamlGenerator
from tools.binance_date_generator import BinanceDateGenerator 
from tools.constants import Constants as Binance
from tools.constants import RelativePath
from tools.str_short_to_complete import str_short_to_complete as str_complete
from tools.show_datetime_execution import show_datetime_execution
from tools.terminal_title_generator import terminal_title_generator
from api_client.binance_api_client import BinanceApiClient
from tools.os_environment import os_environment
from container.binance_data_container import BinanceDataContainer
import sys


if __name__ == "__main__":

    binance_api_settings = DataYamlGenerator(yaml_file= RelativePath.BINANCE_API_SETTINGS)
    binance_api_client = BinanceApiClient()
    binance_data_application = BinanceDataApplication()    

    container = BinanceDataContainer(
        is_terminal_execution= True,
        binance_api_settings= binance_api_settings,
        binance_api_client= binance_api_client,
        binance_data_application= binance_data_application,
        command_arguments=sys.argv
    )

    container.execute()