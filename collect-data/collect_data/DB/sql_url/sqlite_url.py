from sqlalchemy.engine import URL

class SqliteUrl:
    
    def __init__(self, params):
        self.url = URL.create(
            drivername= params['drivername'],
            database= params['database']
        )
    
    def get_url(self):
        return self.url