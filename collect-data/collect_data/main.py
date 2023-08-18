from binance import Client
from application.binance_loader import BinanceLoader
from tools.constants.destination_source import DestinationSource as ds
bl = BinanceLoader(
    destination_source= ds.POSTGRES,
    table_name= 'bitcoin-last-day',
    simbol= "BTCUSDT",
    interval= Client.KLINE_INTERVAL_5MINUTE,
    start= "1 day ago UTC"
    )

bl.generate()
