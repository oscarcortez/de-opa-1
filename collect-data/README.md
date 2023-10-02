# Collect data
## how to run the application

### Options
### For historical data

Historical data will store data from the begining to 1 day before today, frecuency: 1 day

poetry run python3 main.py --type_data historical --printer true

### For streaming data

Streaming will store data from 1 day ago, frecuency: 5 minutes

poetry run python3 main.py --type_data streaming --printer true

poetry run main.py

### For updating streaming data

poetry run python3 cron_main.py --type_data update --printer true
