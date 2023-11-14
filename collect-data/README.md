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

### For FASTAPI 
go to de-opa1/collect-data and run docker-compose up -d
Fastapi then running on: http://localhost:8000/docs