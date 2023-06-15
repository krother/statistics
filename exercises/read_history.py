"""
convert raw historical data from coingecko to pandas
"""
import json
from pprint import pprint
import pandas as pd
from datetime import datetime


j = json.load(open("btc_history.json"))
prices = j["prices"]

def to_timestamp(ts):
    ts = ts/1000
    return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

df = pd.DataFrame(prices, columns=["time", "btc"])
df["time"] = df["time"].apply(to_timestamp)
print(df)
df.to_csv("bitcoin.csv", index=False)
