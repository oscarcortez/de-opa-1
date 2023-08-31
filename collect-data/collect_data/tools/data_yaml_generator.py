import yaml
from tools.constants import AbsolutePath
from tools.os_environment import os_environment

class DataYamlGenerator:
    
    def __init__(self, yaml_file, environment = os_environment()):

        path = ''
        if environment == 'production':
            path = AbsolutePath.APP_PROD
        self.yaml_file = f'{path}{yaml_file}'

    def set_yaml_file(self, yaml_file):

        self.yaml_file = yaml_file

    def get_values(self, section):

        with open(self.yaml_file, 'r') as file:
            self.data_file = yaml.safe_load(file)
        section_data = self.data_file[section]

        return section_data
