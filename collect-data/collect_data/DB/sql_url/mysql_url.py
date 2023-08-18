from sqlalchemy.engine import URL

class MysqlUrl:
    
    def __init__(self):        
        self.url = URL.create(
            drivername="pymysql",
            username='root',
            password='123456',
            host='192.168.230.133',
            port=3306,
            database='opa-binance'
        )
    
    def get_url(self):
        return self.url