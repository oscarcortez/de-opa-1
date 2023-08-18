from sqlalchemy.engine import URL

class SqliteUrl:
    
    def __init__(self):
        self.url = URL.create(
            drivername="sqlite",
            database="opa-binance.db"
        )
    
    def get_url(self):
        return self.url