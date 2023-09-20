from tools.os_environment import os_environment


class RelativePath:
    BINANCE_API_SETTINGS = "config/api_binance_settings.yaml"
    ENV_SETTINGS = f"config/{os_environment()}.settings.yaml"
    SECRETS = "config/secrets.yaml"


class AbsolutePath:
    APP_DEV = "/home/oscar/git-repos/de-opa-1/collect-data/collect_data/"


class Section:
    BINANCE = "binance"


class File:
    JSON = "json"
    CSV = "csv"


class DB:
    POSTGRES = "postgres"
    MYSQL = "mysql"
    SQLITE = "sqlite"
    MONGODB = "mongodb"


class Binance:
    HISTORICAL_DATA = "binance_historical_data"
    STREAMING_DATA = "binance_streaming_data"
    NAME = "binance"


class Constants:
    pass


class DF:
    COL_0 = "open_time"
    COL_1 = "open_price"
    COL_2 = "high_price"
    COL_3 = "low_price"
    COL_4 = "close_price"
    COL_5 = "volume"
    COL_6 = "close_time"
    COL_7 = "quote_asset_volume"
    COL_8 = "number_of_trades"
    COL_9 = "taker_buy_base_asset_volume"
    COL_10 = "taker_buy_quote_asset_volume"
    COL_11 = "ignore"
