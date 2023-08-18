
from .sql_url.mysql_url import MysqlUrl
from .sql_url.postgres_url import PostgresUrl
from .sql_url.sqlite_url import SqliteUrl

class UrlFactory:
    def __init__(self, engine):
        mysql = MysqlUrl()
        postgres = PostgresUrl()
        sqlite = SqliteUrl()
        self.urls = {
            "mysql": mysql.get_url(),
            "postgres": postgres.get_url(),
            "sqlite": sqlite.get_url()
        }
        self.engine = engine
    
    def get_url(self):
        return self.urls[self.engine]
    
    