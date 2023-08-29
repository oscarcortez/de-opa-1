import os
from tools.constants import Constants as C

class EnvSelector:

    def __init__(self):
        self.environment = os.getenv('CRYPTOBOT_ENV', 'development')

    def get_env_settings_path(self):
        result = {
            'production': f'{C.PATH_LINUX}{C.PATH_CONFIG_PROD_SETTINGS_YAML}',
            'development': f'{C.PATH_CONFIG_DEV_SETTINGS_YAML}'
        }
        return result[self.environment]

    def get_settings_path(self):
        result = {
            'production': f'{C.PATH_LINUX}{C.PATH_CONFIG_SETTINGS_YAML}',
            'development': f'{C.PATH_CONFIG_SETTINGS_YAML}'
        }
        return result[self.environment]
    
    def get_history_path(self):
        result = {
            'production': f'{C.PATH_LINUX}{C.PATH_HISTORY_CSV}',
            'development': f'{C.PATH_HISTORY_CSV}'
        }
        return result[self.environment]