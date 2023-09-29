from abc import ABC, abstractmethod


class BinanceDataRepository(ABC):
    @abstractmethod
    def set_table_name(self, table_name):
        pass

    @abstractmethod
    def load_from_dataframe(self, df_data, table_name):
        pass

    @abstractmethod
    def add_df(self, df_new):
        pass

    @abstractmethod
    def exists(self):
        pass
