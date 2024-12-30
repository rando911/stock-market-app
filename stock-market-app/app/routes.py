from flask import Blueprint, render_template, request
from app.services.stock_service import get_stock_data  # Ensure this function is in stock_service.py

bp = Blueprint('main', __name__)

@bp.route("/", methods=["GET", "POST"])
def index():
    stock_code = request.form.get("stock_code", "AAPL")  # Default to AAPL if no stock code is provided
    stock_data = get_stock_data(stock_code)  # Get stock data (including candlestick chart)

    return render_template("index.html", stock_code=stock_code, stock_data=stock_data)
