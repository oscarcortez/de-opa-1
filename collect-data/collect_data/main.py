from application.binance_loader import BinanceLoader
from config.data_yaml_generator import DataYamlGenerator
from tools.binance_date_generator import BinanceDateGenerator 
from tools.constants import Constants as C
import sys

section = C.YAML_SECTION_BINANCE_STREAMING_DATA
if len(sys.argv) > 1:
    section = sys.argv[1]

dyg = DataYamlGenerator(yaml_file= C.PATH_CONFIG_SETTINGS_YAML)
params = dyg.get_values(section)

bdg = BinanceDateGenerator(type_data= section)

bl = BinanceLoader(
    destination_source= params['destination_source'],
    table_name= params['table_name'],
    symbol= params['symbol'],
    interval= params['interval'],
    start= bdg.get_start(),
    end= bdg.get_end()
    )

bl.generate()
