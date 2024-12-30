import requests
from config import Config  # To get the API key from config
import plotly.graph_objects as go

def get_stock_data(stock_code):
    """
    Fetches stock data for the given stock symbol using Alpha Vantage API.

    :param stock_code: The stock symbol (e.g., 'AAPL', 'TSLA')
    :return: A dictionary containing stock data or error message
    """
    # Fetch API key from config
    api_key = Config.STOCK_API_KEY
    url = "https://www.alphavantage.co/query"

    # Request parameters for the Alpha Vantage API
    params = {
        "function": "TIME_SERIES_DAILY",  # Daily stock data
        "symbol": stock_code,
        "apikey": api_key
    }

    # Make the API request
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (status codes 4xx/5xx)
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {e}"}

    # Parse the response data (JSON)
    data = response.json()

    # Check if 'Time Series (Daily)' data exists in the response
    if "Time Series (Daily)" not in data:
        return {"error": "No data available for this stock code."}

    # Extract the daily time series data
    stock_data = data["Time Series (Daily)"]

    # Prepare data for the candlestick chart
    dates = []
    opens = []
    highs = []
    lows = []
    closes = []

    # Get the last 30 days of data (or adjust for a different period)
    for date, values in list(stock_data.items())[:30]:
        dates.append(date)
        opens.append(float(values["1. open"]))
        highs.append(float(values["2. high"]))
        lows.append(float(values["3. low"]))
        closes.append(float(values["4. close"]))

    # Create a candlestick chart
    fig = go.Figure(data=[go.Candlestick(
        x=dates,
        open=opens,
        high=highs,
        low=lows,
        close=closes,
        name="Stock Candlestick"
    )])

    # Update layout
    fig.update_layout(
        title=f'{stock_code} - Candlestick Chart',
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        xaxis_rangeslider_visible=False  # Hides range slider
    )

    # Return the Plotly chart HTML div
    return fig.to_html(full_html=False)
