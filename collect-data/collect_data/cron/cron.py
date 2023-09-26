import schedule
import urllib.request, json
import time
import pandas as pd
from binance import Client
#from tools.yaml_reader import YAMLReader
#from tools.constants import Section
from cron.creds import binance

#client = Client(api_key, api_secret)
api_key = binance(api_key)
print(api_key)

#secrets_settings= YAMLReader
#secrets_settings = secrets_settings

#credentials = secrets_settings.get_values(section = Section.BINANCE)
#API_KEY = credentials['api_key']
#API_SECRET = credentials['api_secret']

#print(API_KEY)