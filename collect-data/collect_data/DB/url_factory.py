
from .sql_connections.mysql_connection import MysqlConnection
from .sql_connections.postgres_connection import PostgresConnection
from .sql_connections.sqlite_connection import SqliteConnection
from config.data_yaml_generator import DataYamlGenerator
from tools.constants import Constants as C
from tools.env_selector import EnvSelector

class UrlFactory:

    def __init__(self, engine):        
        
        env = EnvSelector()
        env_settings = env.get_env_settings_path()
        self.dyg = DataYamlGenerator(yaml_file= env_settings)
        self.engine = engine
    
    def get_url(self):

        params= self.dyg.get_values(section=self.engine)

        if self.engine == 'mysql':
            mysql = MysqlConnection(params)
            return mysql.get_url()
        elif self.engine == 'postgres':
            postgres = PostgresConnection(params)
            return postgres.get_url()
        elif self.engine == 'sqlite':
            sqlite = SqliteConnection(params)
            return sqlite.get_url()
        
    
    