from tools.os_environment import os_environment
from application.binance_data_application import BinanceDataApplication
from tools.constants import Binance
from tools.yaml_reader import YAMLReader
from tools.str_short_to_complete import str_short_to_complete as str_complete


class ApiBinanceDataContainer:
    def __init__(
        self,
        binance_api_settings: YAMLReader,
        binance_data_application: BinanceDataApplication,
    ):
        self.environment = os_environment()
        self.binance_api_settings = binance_api_settings
        self.binance_data_application = binance_data_application

    def build_binance_data_application(self, table_name):
        self.common_params = self.binance_api_settings.get_values(Binance.NAME)
        self.binance_data_application.table_name = table_name
        self.binance_data_application.destination_source = str_complete(
            self.common_params["destination_source"]
        )
        self.binance_data_application.set_binance_data_repository()

        return self.binance_data_application

    def get_destination_source(self):
        return self.common_params["destination_source"]
