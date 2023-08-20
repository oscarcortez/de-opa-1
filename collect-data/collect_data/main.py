from binance import Client
from application.binance_loader import BinanceLoader
from config.data_yaml_generator import DataYamlGenerator
from tools.constants import Constants as C

dyg = DataYamlGenerator(yaml_file= C.PATH_CONFIG_SETTINGS_YAML)
params = dyg.get_values(section= C.YAML_SECTION_BINANCE_LOADER)

bl = BinanceLoader(
    destination_source= params['destination_source'],
    table_name= params['table_name'],
    symbol= params['symbol'],
    interval= params['interval'],
    start= params['start']
    )

bl.generate()
