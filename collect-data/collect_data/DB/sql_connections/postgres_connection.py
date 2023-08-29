from sqlalchemy.engine import URL
from config.data_yaml_generator import DataYamlGenerator

class PostgresConnection:
    
    def __init__(self, params):
        
        self.url = URL.create(
            drivername=params['drivername'],
            username=params['username'],
            password=params['password'],
            host=params['host'],
            port=params['port'],
            database=params['database']
        )
    
    def get_url(self):
        return self.url