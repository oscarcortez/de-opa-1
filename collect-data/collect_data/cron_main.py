
from cron.binance_data_updater import BinanceDataUpdater
from binance import Client
from tools.yaml_reader import YAMLReader
from tools.constants import RelativePath
from api_client.binance_api_client import BinanceApiClient
import schedule
import urllib.request, json
import time

def start():
    schedule.every(60).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

def job():

    if __name__ == "__main__":

        container = BinanceDataUpdater(
            binance_api_client = BinanceApiClient(),
            binance_client = Client(),
            secrets_settings = YAMLReader(yaml_file= RelativePath.SECRETS),
            binance_api_settings = YAMLReader(yaml_file=RelativePath.BINANCE_API_SETTINGS)
        )

        container.execute()

start()
