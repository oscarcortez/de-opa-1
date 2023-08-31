from sqlalchemy.engine import URL
from tools.data_yaml_generator import DataYamlGenerator
from tools.constants import Constants as C, RelativePath, DB

def mysql_url_connection():

    dyg = DataYamlGenerator(yaml_file= RelativePath.ENV_SETTINGS)
    params = dyg.get_values(section= DB.MYSQL)
    url = URL.create(
        drivername= params['drivername'],            
        username= params['username'],
        password= params['password'],
        host= params['host'],
        port= params['port'],
        database= params['database']
    )
    
    return url