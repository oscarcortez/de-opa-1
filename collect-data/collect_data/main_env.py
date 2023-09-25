from tools.os_environment import os_environment
import os

import datetime

print("environment:", os_environment(), end=", ")
print("login:", os.getlogin(), end=", ")
print("datetime:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
