#from datetime import datetime
from tools.yaml_reader import YAMLReader
from binance import Client
from tools.constants import Section


class BinanceDataUpdater:
    
    def __init__(self,
                 binance_client: Client,
                 secrets_settings: YAMLReader
                 ):
        self.secrets_settings = secrets_settings
        self.binance_client = binance_client

    def set_binance_client(self):

        credentials = self.secrets_settings.get_values(section = Section.BINANCE)
        self.binance_client.API_KEY = credentials['api_key']
        self.binance_client.API_SECRET = credentials['api_secret']
        
        print(self.binance_client.API_KEY)


   
    
    

   
        

    def execute_application(self):
        self.set_binance_client()
        

    def execute(self):
        self.execute_application()





    