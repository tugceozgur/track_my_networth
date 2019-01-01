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

        with open('crypto_holdings.json', 'r') as f:
            crypto_holdings = json.load(f)

        for coin in crypto_holdings:
            total_worth += float(CoinWorth.get_coin_price(coin))*float(crypto_holdings[coin])

        return total_worth