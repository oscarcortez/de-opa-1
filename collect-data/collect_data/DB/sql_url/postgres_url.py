from sqlalchemy.engine import URL

class PostgresUrl:
    
    def __init__(self):
        self.url = URL.create(
            drivername="postgresql",
            username='postgres',
            password='123456',
            host='localhost',
            port=5437,
            database='opa-binance'
        )
    
    def get_url(self):
        return self.url