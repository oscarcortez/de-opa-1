import os


def os_environment():
    return os.getenv("CRYPTOBOT_ENV", "local")


def os_login():
    return os.getlogin()
