
from cron.binance_data_updater import BinanceDataUpdater
from binance import Client
from tools.yaml_reader import YAMLReader
from tools.constants import RelativePath

if __name__ == "__main__":

    container = BinanceDataUpdater(
        #binance_api_client = BinanceApiClient(),
        binance_client = Client(),
        secrets_settings = YAMLReader(yaml_file= RelativePath.SECRETS)
    )

    container.execute()

