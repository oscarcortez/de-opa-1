from application.binance_data_application import BinanceDataApplication
from tools.yaml_reader import YAMLReader
from tools.constants import RelativePath
from api_client.binance_api_client import BinanceApiClient
from container.binance_data_container import BinanceDataContainer
from tools.history import History
from binance import Client
from tools.args_reader import ArgsReader

if __name__ == "__main__":
    local_settings = YAMLReader(yaml_file=RelativePath.ENV_SETTINGS)
    tld = local_settings.get_values("binance")["tld"]
    container = BinanceDataContainer(
        binance_api_settings=YAMLReader(RelativePath.BINANCE_API_SETTINGS),
        binance_api_client=BinanceApiClient(),
        binance_client=Client(tld=tld),
        binance_data_application=BinanceDataApplication(),
        history=History(RelativePath.ENV_SETTINGS),
        command_arguments=ArgsReader(),
        secrets_settings=YAMLReader(yaml_file=RelativePath.SECRETS),
    )

    container.execute()
