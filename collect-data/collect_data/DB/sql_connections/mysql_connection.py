from sqlalchemy.engine import URL

class MysqlConnection:
    
    def __init__(self, params):

        self.url = URL.create(
            drivername= params['drivername'],            
            username= params['username'],
            password= params['password'],
            host= params['host'],
            port= params['port'],
            database= params['database']
        )
    
    def get_url(self):
        return self.url