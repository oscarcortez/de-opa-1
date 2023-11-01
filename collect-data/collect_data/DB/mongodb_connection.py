from pymongo import MongoClient
from tools.yaml_reader import YAMLReader
from tools.constants import DB, RelativePath

dyg = YAMLReader(yaml_file=RelativePath.ENV_SETTINGS)
params = dyg.get_values(section=DB.MONGODB)

MONGO_HOST = params['host'] 
MONGO_PORT = params['port']
MONGO_DB = params['drivername']
MONGO_USER = params['username']
MONGO_PASS = params['password']

uri = "mongodb://{}:{}@{}:{}/{}?authSource=admin".format(MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT, MONGO_DB)
mongo_client = MongoClient(uri)
mongo_db = mongo_client[params["database"]]