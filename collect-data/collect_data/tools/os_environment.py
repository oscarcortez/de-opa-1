import os

def os_environment():
    
    return os.getenv('CRYPTOBOT_ENV', 'development')

def os_login():

    return os.getlogin()