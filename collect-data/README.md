# Collect data
## how to run the application

### Options
### For historical data
Historical data will store data from the begining to 1 day before today, frecuency: 1 day
poetry run main.py binance_historical_data

### For streaming data
Streaming will store data from 1 day ago, frecuency: 5 minutes
poetry run main.py binance_streaming_data
poetry run main.py