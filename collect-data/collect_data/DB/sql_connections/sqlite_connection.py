from sqlalchemy.engine import URL
from tools.data_yaml_generator import DataYamlGenerator
from tools.constants import RelativePath, DB

def sqlite_url_connection():

    dyg = DataYamlGenerator(yaml_file= RelativePath.ENV_SETTINGS)
    params = dyg.get_values(section= DB.SQLITE)
    url = URL.create(
        drivername= params['drivername'],
        database= params['database']
    )
    
    return url