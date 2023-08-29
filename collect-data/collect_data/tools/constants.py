class Constants:

    JSON = 'json'
    CSV = 'csv'

    DB_POSTGRES = 'postgres'
    DB_MYSQL = 'mysql'
    DB_SQLITE = 'sqlite'

    PATH_LINUX = '/home/oscar/git-repos/de-opa-1/collect-data/collect_data/'
    PATH_CONFIG_PROD_SETTINGS_YAML = 'config/settings.prod.yaml'
    PATH_CONFIG_DEV_SETTINGS_YAML = 'config/settings.dev.yaml'
    PATH_CONFIG_SETTINGS_YAML = 'config/settings.yaml'

    PATH_CONFIG_SECRETS_YAML = 'config/secrets.yaml'
    PATH_HISTORY_CSV = 'data/history.csv'

    YAML_SECTION_BINANCE_HISTORICAL_DATA= 'binance_historical_data'
    YAML_SECTION_BINANCE_STREAMING_DATA= 'binance_streaming_data'
    YAML_SECTION_BINANCE = 'binance'

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