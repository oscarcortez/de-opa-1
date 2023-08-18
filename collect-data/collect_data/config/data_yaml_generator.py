import yaml
class DataYamlGenerator:
    
    def __init__(self, yaml_file, section):
        self.section = section
        with open(yaml_file, 'r') as file:
            self.data_file = yaml.safe_load(file)
    
    def get_values(self, keys):
        result = dict.fromkeys(keys)
        result.update(self.data_file[self.section])
        return result
