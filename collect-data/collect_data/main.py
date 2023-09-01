from application.binance_data_application import BinanceDataApplication
from tools.yaml_reader import YAMLReader
from tools.constants import RelativePath
from api_client.binance_api_client import BinanceApiClient
from container.binance_data_container import BinanceDataContainer
from tools.history import History
from binance import Client
from tools.constants import Section
from tools.command_line_arguments import CommandLineArguments
import sys

if __name__ == "__main__":

    path_settings= RelativePath.ENV_SETTINGS
    container = BinanceDataContainer(        
        binance_api_settings= YAMLReader(yaml_file= RelativePath.BINANCE_API_SETTINGS),
        binance_api_client= BinanceApiClient(),
        binance_client = Client(),
        binance_data_application= BinanceDataApplication(),
        history= History(path_settings),
        command_arguments=CommandLineArguments(sys.argv),
        secrets_settings= YAMLReader(yaml_file= RelativePath.SECRETS)
    )

    container.execute()