import requests
from flask import current_app

def get_stock_data(symbol):
    params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": symbol,
        "apikey": current_app.config['STOCK_API_KEY']
    }
    response = requests.get(current_app.config['STOCK_API_URL'], params=params)

    if response.status_code == 200:
        data = response.json()
        if "Time Series (Daily)" in data:
            # Process the data into a simpler format
            time_series = data["Time Series (Daily)"]
            processed_data = {
                "symbol": symbol,
                "prices": [
                    {"date": date, "close": float(details["4. close"])}
                    for date, details in time_series.items()
                ]
            }
            return processed_data
    return None
