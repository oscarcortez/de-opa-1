# Predictive Bitcoin Value Tracker

## Introduction

The Predictive Bitcoin Value Tracker accesses the Binance API and, with the use of machine learning, displays the historical as well as predicted future values of Bitcoin. This tool empowers users to explore past trends and gain insights into potential future changes in the Bitcoin market.

## Features

- Historical Bitcoin value visualization
- Streaming Bitcoin value visualization
- Predictive analysis based on machine learning algorithms
- User-friendly interface via Dash for easy navigation and data interpretation

## Installation

Follow these steps to set up the Predictive Bitcoin Value Tracker:

1. **Clone the Repository:**
   ```bash
   git clone https://git@github.com:oscarcortez/de-opa-1.git
   cd collect-data
   cd collect_data
   ```

2. **Install Poetry:**
   Poetry is used for managing dependencies in this project. If you don't have Poetry installed, follow the installation guide at https://python-poetry.org/docs/#installation for instructions.

3. **Install Docker:**
   Docker is required for containerization. Install Docker by following the installation guide at https://docs.docker.com/get-docker/.

4. **Install Dependencies:**
   ```bash
   poetry install
   ```

## Configuration

To configure the application, follow these steps:

1. **Create a Binance Account and Obtain API Key:**
   - If you don't have a Binance account, create one at https://www.binance.com (international users) or https://www.binance.us (USA users).
   - After logging in, navigate to your account settings and create a new API key. Ensure you enable the necessary permissions for accessing historical and real-time data.

2. **Create the file `secrets.yaml`:**
   - Create a document called `secrets.yaml` file in the project directory under the config folder.
   - Open the file using a text editor.
   

3. **Include Binance API Key and Secret:**
   - Add your Binance API key and secret to the `secrets.yaml` file.
   - Add the following text to the file:
	binance:
		api_key: followed by your api_key
		api_secret: followed by your api_secret
   - Save the file.

4. **Configure international or United States setting:**
   - Open the local_settings.yaml file and set the tld setting to "com" or "us" based on your geographic location.
   - Save the file.

Your configuration is now complete. Keep your API key and secret confidential and do not share them publicly.

## Usage

## Create Docker Containers
   - Navigate to the `de-opa1/collect-data` directory.
   - Run the following command:
     ```bash
     docker compose up -d
     ```

## Historical Data
   - Navigate to the `de-opa1/collect-data/collect_data` directory.
   - Run the following command:
     ```bash
     poetry run python3 main.py --type_data historical --printer true
     ```

## Streaming Data
   - Navigate to the `de-opa1/collect-data/collect_data` directory.
   - Run the following command:
     ```bash
     poetry run python3 main.py --type_data streaming --printer true
     ```

## For FASTAPI 
   - Create the Docker containers
   - Access http://localhost:8000/docs

## Access the Dashboard
   - Once the application is running, go to http://localhost:8050 to access the dashboard.



