import json
import requests
from bs4 import BeautifulSoup
from semantic_kernel.skill_definition import sk_function

class Stocks:
    # This is the decorator that will register your function to the semantic kernel
    @sk_function(
        description="Get Stocks live data from Dubai Financial Market",
        name="GetStocks",
        input_description="the stock ticker name to get the live data for",
    )
    def get_stocks(self, ticker: str) -> str:
        url ="https://api2.dfm.ae/mw/v1/stocks"
        api_result = requests.get(url).json()
        matching_stocks = [stock for stock in api_result if stock["id"] == ticker]
        if matching_stocks:
            return json.dumps(matching_stocks)
        else:
            return "Not found"
