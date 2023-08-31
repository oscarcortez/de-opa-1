from sqlalchemy.engine import URL
from config.data_yaml_generator import DataYamlGenerator
from tools.constants import Constants as C, RelativePath, DB
from tools.env_selector import EnvSelector

def postgres_url_connection():

    env = EnvSelector()
    dyg = DataYamlGenerator(yaml_file= RelativePath.ENV_SETTINGS)
    params = dyg.get_values(section= DB.POSTGRES)
    url = URL.create(
        drivername=params['drivername'],
        username=params['username'],
        password=params['password'],
        host=params['host'],
        port=params['port'],
        database=params['database']
    )

    return url