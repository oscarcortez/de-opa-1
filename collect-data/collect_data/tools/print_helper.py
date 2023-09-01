
def print_helper():
    print('''
Executions: 

Windows:
\tpoetry run main.py historical false
\tpoetry run main.py streaming false
\tpoetry run main.py historical true
\tpoetry run main.py streaming true

\tFirst argument is the execution file
\tSecond argument is the type of data to be extracted from Binance Api
\tThird argument is to know if the app run in background or it was executed manually
  

To configure variables related to binance Api:
  
\tconfig/api_binance_settings.yaml
\tdestination source: [postgres, sqlite, mysql, mongodb, json, csv]
\tinterval: [1d, 5m, 1m, 1h]

''')