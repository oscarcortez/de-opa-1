import schedule
import urllib.request, json
import time
import pandas as pd
from binance import Client
from tools.constant import Section
from config.secrets import binance

api_key = binance(api_key)
print(api_key)

#client = Client(api_key, api_secret)

