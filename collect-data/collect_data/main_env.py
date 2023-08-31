from tools.env_selector import EnvSelector

env = EnvSelector()
print('environment:', env.environment)

class square:
    def __init__(self):
        print('Im square')

class circle: 
    def __init__(self):
        print('Im circle')

class_name_string= 'square'
class_name = globals()[class_name_string]
form = class_name()

import os

print('login: ',os.getlogin())