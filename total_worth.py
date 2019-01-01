import requests
import json

class CryptoWorth:
    _base_url = "https://api.coinmarketcap.com/v1/ticker/"

    @classmethod
    def get_coin_price(self,coin_name):
        url_extension = coin_name
        resp = requests.get(self._base_url + url_extension)
        return resp.json()[0]['price_usd']

    @classmethod
    def calculate_crypto_worth(self):
        crypto_worth = 0

        #parse crypto holdings
        with open('crypto_holdings.json', 'r') as f:
            crypto_holdings = json.load(f)

        #get total crypto worth
        for coin in crypto_holdings:
            crypto_worth += float(self.get_coin_price(coin))*float(crypto_holdings[coin])

        return crypto_worth

class ExchangeCash:

    @classmethod
    def to_usd(self):
        cash_worth = 0

        exchange_rates = requests.get("https://api.exchangeratesapi.io/latest?base=USD").json()['rates']

        #parse cash holdings
        with open('cash_holdings.json', 'r') as f:
            cash_holdings = json.load(f)

        #get total cash worth
        for cash in cash_holdings:
            cash_worth += float(exchange_rates[cash])*float(cash_holdings[cash])

        return cash_worth

        