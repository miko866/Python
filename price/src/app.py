__author__ = 'miko'

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.fust.ch/de/p/pc-tablet-handy/notebook-macbook-laptop/apple-macbook/apple/macbook-pro-13-silber-8311543.html")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("div", {"class": "endprice", "itemprop": "price"})
string_price = element.text.strip()

price_without_symbol = string_price[:-2]
clear_price = price_without_symbol.replace("’", "")
price = int(clear_price)

if price < 1500:
    print("You schould buy the NB")
    print("The current price is {}".format(price))
else:
    print("Do not buy, it's too expensive!")
    print("The current price is {}".format(price))
