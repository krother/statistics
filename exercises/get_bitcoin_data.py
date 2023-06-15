"""
download bitcoin data from the API of coingecko.com
and store it in a CSV file

API docs: https://www.coingecko.com/en/api/documentation
"""
import requests
from pprint import pprint


BASE_URL = "https://api.coingecko.com/api/v3/"

# check whether server is alive
#response = requests.get(BASE_URL + "ping")
#print(response.status_code)
#print(response.json())

# get list of available cryptocurrencies
response = requests.get(BASE_URL + "coins/list")
coins = response.json()
print(coins)
pprint([c for c in coins if c["name"].startswith("bitcoin")])

# get historical prices
response = requests.get(BASE_URL + "/coins/bit/market_chart/range")
