from pymongo import MongoClient
from tools.yaml_reader import YAMLReader
from tools.constants import DB, RelativePath

dyg = YAMLReader(yaml_file=RelativePath.ENV_SETTINGS)
params = dyg.get_values(section=DB.MONGODB)

mongo_client = MongoClient(
                host=params['host'],
                port=params['port'],
                authSource="admin")
mongo_db = mongo_client[params["database"]]
