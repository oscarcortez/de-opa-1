from tools.binance_date_generator import BinanceDateGenerator
from tools.os_environment import os_environment
from tools.str_short_to_complete import str_short_to_complete as str_complete
from tools.string_to_bool import string_to_bool
from tools.decorators.logger import logger
from tools.decorators.timer import timer
from api_client.binance_api_client import BinanceApiClient
from application.binance_data_application import BinanceDataApplication
from tools.constants import Binance
from tools.print_terminal_title import print_terminal_title
from tools.print_table import print_table
from tools.history import History
from datetime import datetime
from tools.yaml_reader import YAMLReader
from tools.command_line_arguments import CommandLineArguments
from binance import Client
from tools.constants import Section
from tools.print_helper import print_helper

class BinanceDataContainer:
    
    def __init__(self,                  
                 binance_api_settings: YAMLReader,
                 binance_api_client: BinanceApiClient,
                 binance_client: Client,
                 binance_data_application: BinanceDataApplication,
                 history: History,
                 command_arguments: CommandLineArguments,
                 secrets_settings: YAMLReader,
                 is_terminal_execution = 'false',
                 is_helper = False
                 ):
        
        self.environment = os_environment()
        self.is_terminal_execution = is_terminal_execution
        self.binance_api_settings = binance_api_settings
        self.binance_api_client = binance_api_client
        self.binance_data_application = binance_data_application
        self.command_arguments = command_arguments
        self.history = history
        self.secrets_settings = secrets_settings
        self.binance_client = binance_client
        self.is_helper = is_helper

    def set_binance_client(self):

        credentials = self.secrets_settings.get_values(section = Section.BINANCE)
        self.binance_client.API_KEY = credentials['api_key']
        self.binance_client.API_SECRET = credentials['api_secret']

    def read_terminal_arguments(self):
        
        self.type_data = str_complete(self.command_arguments.get_type_data())
        self.is_terminal_execution = str(self.command_arguments.get_show_details())
        self.is_helper = self.command_arguments.is_helper()

    def get_common_params(self):
        self.common_params = self.binance_api_settings.get_values(Binance.NAME)
    
    def get_type_data_params(self):
        self.type_data_params = self.binance_api_settings.get_values(self.type_data)

    def get_range_dates(self):

        bdg = BinanceDateGenerator(self.type_data)
        self.start_range = bdg.get_start()
        self.end_range = bdg.get_end()

    def build_binance_api_client(self):        
        
        self.binance_api_client.client = self.binance_client
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
        
        print_terminal_title(show= string_to_bool(self.is_terminal_execution))

    def show_pretty_history(self):
        
        titles = ['Type Data', 'Date', 'Rows', 'Evironment', 'Destination', 'Symbol']
        values = [
            self.type_data_params['table_name'],
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            self.dataframe.shape[0],
            self.environment,
            self.common_params['destination_source'],
            self.common_params['symbol']
        ]
        print_table(titles, values, string_to_bool(self.is_terminal_execution))

        if not string_to_bool(self.is_terminal_execution):
            
            print(f'\n{values}')
    
    def save_history(self):
        
        self.history.add(
            self.type_data_params['table_name'],
            datetime= datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            rows= self.dataframe.shape[0],
            environment = self.environment,
            destination_source = self.common_params['destination_source'],
            symbol = self.common_params['symbol'],
        )        

    def execute_helper(self):

        print_terminal_title(show= True)
        print_helper()
        
    @timer
    @logger
    def execute_application(self):

        
        self.show_details()
        self.get_common_params()
        self.get_type_data_params()
        self.get_range_dates()
        self.build_binance_api_client()
        self.build_binance_data_application()
        self.get_dataframe()
        self.load_from_dataframe()
        self.save_history()
        self.show_pretty_history()

    def execute(self):
        
        self.read_terminal_arguments()

        if self.is_helper:
            self.execute_helper()
        else:
            self.execute_application()