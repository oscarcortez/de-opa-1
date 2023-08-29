
from .sql_url.mysql_url import MysqlUrl
from .sql_url.postgres_url import PostgresUrl
from .sql_url.sqlite_url import SqliteUrl
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
            mysql = MysqlUrl(params)
            return mysql.get_url()
        elif self.engine == 'postgres':
            postgres = PostgresUrl(params)
            return postgres.get_url()
        elif self.engine == 'sqlite':
            sqlite = SqliteUrl(params)
            return sqlite.get_url()
        
    
    