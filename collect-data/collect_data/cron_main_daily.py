
from binance import Client
from application.binance_data_application import BinanceDataApplication
from container.binance_data_container import BinanceDataContainer
from tools.history import History
from tools.args_reader import ArgsReader
from tools.yaml_reader import YAMLReader
from tools.constants import RelativePath
from api_client.binance_api_client import BinanceApiClient
import schedule
import time


def start():
    schedule.every(60 * 60 * 24).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


def job():

    if __name__ == "__main__":

        container = BinanceDataContainer(
            binance_api_settings=YAMLReader(RelativePath.BINANCE_API_SETTINGS),
            binance_api_client=BinanceApiClient(),
            binance_client=Client(),
            binance_data_application=BinanceDataApplication(),
            history=History(RelativePath.ENV_SETTINGS),
            command_arguments=ArgsReader(),
            secrets_settings=YAMLReader(yaml_file=RelativePath.SECRETS),
        )

        container.execute()


start()
