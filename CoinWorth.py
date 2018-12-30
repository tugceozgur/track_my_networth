import requests

class CoinWorth:
    base_url = "https://api.coinmarketcap.com/v1/ticker/"

    @classmethod
    def bitcoin(self):
        url_extension = "bitcoin"
        resp = requests.get(self.base_url + url_extension)
        return resp.json()[0]['price_usd']


