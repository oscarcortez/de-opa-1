from datetime import datetime
from tools.constants import Binance

class BinanceDateGenerator:
    
    def __init__(self, type_data):

        self.type_data = type_data
    
    def get_midnight_today(self):

        current_day = datetime.utcnow()
        start_time = datetime(current_day.year, current_day.month, current_day.day, 0, 0, 0)
        start_time_milliseconds = int(start_time.timestamp() * 1000)
        return str(start_time_milliseconds)

    def get_start(self):
        
        if self.type_data == Binance.HISTORICAL_DATA:
            return '1 Jan, 1990'
        else:
            return self.get_midnight_today()
    
    def get_end(self):
        if self.type_data == Binance.HISTORICAL_DATA:
            return '1 day ago UTC'
        else:
            return None
