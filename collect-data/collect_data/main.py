from application.binance_data_application import BinanceDataApplication
from tools.yaml_reader import YAMLReader
from tools.constants import RelativePath
from api_client.binance_api_client import BinanceApiClient
from container.binance_data_container import BinanceDataContainer
from tools.history import History
from binance import Client
from tools.constants import Section
import sys

if __name__ == "__main__":

    binance_api_settings = YAMLReader(yaml_file= RelativePath.BINANCE_API_SETTINGS)
    
    secrets = YAMLReader(yaml_file= RelativePath.SECRETS)
    binance_credentials = secrets.get_values(section = Section.BINANCE)
    binance_client = Client(binance_credentials['api_key'], binance_credentials['api_secret'])    
    binance_api_client = BinanceApiClient(client= binance_client)
    binance_data_application = BinanceDataApplication()
    path_settings= RelativePath.ENV_SETTINGS
    history = History(path_settings)
    container = BinanceDataContainer(        
        binance_api_settings= binance_api_settings,
        binance_api_client= binance_api_client,
        binance_data_application= binance_data_application,
        history= history,
        command_arguments=sys.argv
    )

    container.execute()