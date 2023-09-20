from pymongo import MongoClient
from tools.yaml_reader import YAMLReader
from tools.constants import DB, RelativePath

dyg = YAMLReader(yaml_file=RelativePath.ENV_SETTINGS)
params = dyg.get_values(section=DB.MONGODB)
mongo_uri = (
    f"{params['drivername']}://{params['username']}:{params['password']}"
    f"@{params['host']}:{params['port']}/admin"
)
mongo_client = MongoClient(mongo_uri)
mongo_db = mongo_client[params["database"]]
