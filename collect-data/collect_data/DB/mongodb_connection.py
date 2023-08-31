from pymongo import MongoClient
from tools.data_yaml_generator import DataYamlGenerator
from tools.constants import DB, RelativePath

dyg = DataYamlGenerator(yaml_file= RelativePath.ENV_SETTINGS)

params = dyg.get_values(section= DB.MONGODB)
client = MongoClient(f"{params['drivername']}://{params['username']}:{params['password']}@{params['host']}:{params['port']}/admin")
mongo_db = client[params['database']]