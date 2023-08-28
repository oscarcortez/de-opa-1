def str_short_to_complete(value):
    result = {
        'streaming': 'binance_streaming_data',
        'historical': 'binance_historical_data',
        'binance_streaming_data': 'binance_streaming_data',
        'binance_historical_data': 'binance_historical_data',
    }

    return result[value]