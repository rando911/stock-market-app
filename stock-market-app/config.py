import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret')
    STOCK_API_URL = "https://www.alphavantage.co/query"
    STOCK_API_KEY = os.getenv('STOCK_API_KEY')
