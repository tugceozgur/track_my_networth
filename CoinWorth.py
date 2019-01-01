import requests

class CoinWorth:
    base_url = "https://api.coinmarketcap.com/v1/ticker/"

    @classmethod
    def bitcoin(self):
        url_extension = "bitcoin"
        resp = requests.get(self.base_url + url_extension)
        return resp.json()[0]['price_usd']

    @classmethod
    def ethereum(self):
        url_extension = "ethereum"
        resp = requests.get(self.base_url + url_extension)
        return resp.json()[0]['price_usd']

    @classmethod
    def decred(self):
        url_extension = "decred"
        resp = requests.get(self.base_url + url_extension)
        return resp.json()[0]['price_usd']


    @classmethod
    def bitcoin_cash(self):
        url_extension = "bitcoin-cash"
        resp = requests.get(self.base_url + url_extension)
        return resp.json()[0]['price_usd']

    @classmethod
    def ripple(self):
        url_extension = "ripple"
        resp = requests.get(self.base_url + url_extension)
        return resp.json()[0]['price_usd']

    @classmethod
    def qash(self):
        url_extension = "qash"
        resp = requests.get(self.base_url + url_extension)
        return resp.json()[0]['price_usd']