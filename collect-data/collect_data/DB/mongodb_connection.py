from pymongo import MongoClient
from tools.env_selector import EnvSelector
from config.data_yaml_generator import DataYamlGenerator

env = EnvSelector()
env_settings = env.get_env_settings_path()
dyg = DataYamlGenerator(yaml_file= env_settings)
params = dyg.get_values(section= 'mongodb')
client = MongoClient(f"{params['drivername']}://{params['username']}:{params['password']}@{params['host']}:{params['port']}/admin")
mongo_db = client[params['database']]