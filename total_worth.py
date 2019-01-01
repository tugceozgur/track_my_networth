import requests
import json

class CoinWorth:
    _base_url = "https://api.coinmarketcap.com/v1/ticker/"

    @classmethod
    def get_coin_price(self,coin_name):
        url_extension = coin_name
        resp = requests.get(self._base_url + url_extension)
        return resp.json()[0]['price_usd']

class NetWorth:
    @classmethod
    def calculate_net_worth(self):
        total_worth = 0

        with open('holdings.json', 'r') as f:
            holdings = json.load(f)

        for key in holdings:
            print(total_worth)
            total_worth += float(CoinWorth.get_coin_price(key))*float(holdings[key])

        return total_worth