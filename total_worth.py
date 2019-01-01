import requests
import json
import datetime

class CryptoWorth:
    _base_url = 'https://api.coinmarketcap.com/v1/ticker/'

    @classmethod
    def get_coin_price(self,coin_name):
        url_extension = coin_name
        resp = requests.get(self._base_url + url_extension)
        return resp.json()[0]['price_usd']

    @classmethod
    def calculate_crypto_worth(self):
        crypto_worth = 0

        #parse crypto holdings
        try:
            with open('crypto_holdings.json', 'r') as f:
                crypto_holdings = json.load(f)
        except:
            return crypto_worth

        #get total crypto worth
        for coin in crypto_holdings:
            crypto_worth += float(self.get_coin_price(coin))*float(crypto_holdings[coin])

        return crypto_worth

class ExchangeCash:

    @classmethod
    def to_usd(self):
        cash_worth = 0

        exchange_rates = requests.get('https://api.exchangeratesapi.io/latest?base=USD').json()['rates']

        #parse cash holdings
        try:
            with open('cash_holdings.json', 'r') as f:
                cash_holdings = json.load(f)
        except:
            return cash_worth

        #get total cash worth
        for cash in cash_holdings:
            cash_worth += float(cash_holdings[cash])/float(exchange_rates[cash])

        return cash_worth

def get_total_worth():
    return (ExchangeCash.to_usd()+CryptoWorth.calculate_crypto_worth())

def save_total_worth():
    networth = get_total_worth()
    current_date = datetime.date.today().strftime("%B %d, %Y")

    with open('networth.txt', 'a+') as f:
        f.write("{0} {1}\n".format(str(networth), current_date))

    
    