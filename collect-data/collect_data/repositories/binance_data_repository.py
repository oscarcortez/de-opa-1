
from abc import ABC, abstractmethod

class BinanceDataRepository(ABC):
    @abstractmethod
    def load_from_dataframe(self, df_data, table_name):
        pass