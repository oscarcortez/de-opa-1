from tools.binance_date_generator import BinanceDateGenerator
from tools.os_environment import os_environment
from tools.str_short_to_complete import str_short_to_complete as str_complete
from tools.decorators.logger import logger
from tools.decorators.timer import timer
from api_client.binance_api_client import BinanceApiClient
from application.binance_data_application import BinanceDataApplication
from tools.constants import Binance
from tools.terminal_title_generator import terminal_title_generator
from tools.history import History
from datetime import datetime

class BinanceDataContainer:
    
    def __init__(self,                  
                 binance_api_settings,
                 binance_api_client: BinanceApiClient, 
                 binance_data_application: BinanceDataApplication,
                 command_arguments,
                 is_terminal_execution = 'false',
                 ):
        
        self.environment = os_environment()
        self.is_terminal_execution = is_terminal_execution
        self.binance_api_settings = binance_api_settings
        self.binance_api_client = binance_api_client
        self.binance_data_application = binance_data_application
        self.command_arguments = command_arguments
        self.history = History()
    
    def read_terminal_arguments(self):
        if len(self.command_arguments) > 1:
            self.streaming_historical_section = str_complete(self.command_arguments[1])
        if len(self.command_arguments) > 2:
            self.is_terminal_execution = self.command_arguments[2]

    def get_common_params(self):
        self.common_params = self.binance_api_settings.get_values(Binance.NAME)
    
    def get_type_data_params(self):
        self.type_data_params = self.binance_api_settings.get_values(self.streaming_historical_section)

    def get_range_dates(self):
        bdg = BinanceDateGenerator(self.streaming_historical_section)
        self.start_range = bdg.get_start()
        self.end_range = bdg.get_end()

    def build_binance_api_client(self):        
        self.binance_api_client.symbol = self.common_params['symbol']
        self.binance_api_client.interval = self.type_data_params['interval']
        self.binance_api_client.start = self.start_range
        self.binance_api_client.end = self.end_range

    def build_binance_data_application(self):
        self.binance_data_application.table_name = self.type_data_params['table_name']
        self.binance_data_application.destination_source = self.common_params['destination_source']
        self.binance_data_application.set_binance_data_repository()

    def get_dataframe(self):
        self.dataframe = self.binance_api_client.get_dataframe()
    
    def load_from_dataframe(self):
        self.binance_data_application.load_from_dataframe(self.dataframe)

    def show_details(self):
        terminal_title_generator(self.is_terminal_execution)
        print('terminal',self.is_terminal_execution)
    
    def save_history(self):
        self.history.add(
            self.type_data_params['table_name'],
            datetime= datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
            rows= self.dataframe.shape[0],
            environment = self.environment, 
            destination_source = self.common_params['destination_source'],
            symbol = self.common_params['symbol'],
        )
    
    @logger
    @timer
    def execute(self):
        
        self.show_details()
        self.read_terminal_arguments()
        self.get_common_params()
        self.get_type_data_params()
        self.get_range_dates()
        self.build_binance_api_client()
        self.build_binance_data_application()
        self.get_dataframe()
        self.load_from_dataframe()
        self.save_history()
        