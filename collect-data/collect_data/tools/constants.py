from tools.os_environment import os_environment

class RelativePath:
    BINANCE_API_SETTINGS = 'config/api_binance_settings.yaml'
    ENV_SETTINGS = f'config/{os_environment()}.settings.yaml'
    SECRETS = 'config/secrets.yaml'

class AbsolutePath:
    APP_PROD = '/home/oscar/git-repos/de-opa-1/collect-data/collect_data/'

class Section: 
    BINANCE = 'binance'

class File:
    JSON = 'json'
    CSV = 'csv'

class DB:
    POSTGRES = 'postgres'
    MYSQL = 'mysql'
    SQLITE = 'sqlite'
    MONGODB = 'mongodb'

class Binance:
    HISTORICAL_DATA= 'binance_historical_data'
    STREAMING_DATA= 'binance_streaming_data'
    NAME = 'binance'
class Constants:

    PATH_CONFIG_PROD_SETTINGS_YAML = 'config/settings.prod.yaml'
    PATH_CONFIG_DEV_SETTINGS_YAML = 'config/settings.dev.yaml'
    RELATIVE_PATH_SETTINGS = 'config/settings.yaml'

    SECRETS_YAML = 'config/secrets.yaml'
    PATH_HISTORY_CSV = 'data/history.csv'

    SQLITE = 'sqlite'

    DF_COL_0= 'open_time'
    DF_COL_1= 'open_price'
    DF_COL_2= 'high_price'
    DF_COL_3= 'low_price'
    DF_COL_4= 'close_price'
    DF_COL_5= 'volume'
    DF_COL_6= 'close_time'
    DF_COL_7= 'quote_asset_volume'
    DF_COL_8= 'number_of_trades'
    DF_COL_9= 'taker_buy_base_asset_volume'
    DF_COL_10= 'taker_buy_quote_asset_volume'
    DF_COL_11= 'ignore'