import unittest
from total_worth import CryptoWorth
# from total_worth import NetWorth
from total_worth import ExchangeCash

class Test_TestPrices(unittest.TestCase):
    def test_coin_price(self):
        print("Bitcoin price: " + CryptoWorth.get_coin_price("bitcoin"))
        print("Ethereum price: " + CryptoWorth.get_coin_price("ethereum"))
        print("Decred price: " + CryptoWorth.get_coin_price("decred"))
        print("Bitcoin Cash price: " + CryptoWorth.get_coin_price("bitcoin-cash"))
        print("Qash price: " + CryptoWorth.get_coin_price("qash"))
        print("Ripple price: " + CryptoWorth.get_coin_price("ripple"))

    def test_coin_price_calculator(self):
        print("Total Coin Worth: " + str(CryptoWorth.calculate_crypto_worth()))

    def test_all_cash_to_one_currency_exchange(self):
        print("Total Cash Worth in USD: " + str(ExchangeCash.to_usd()))

    def test_total_net_worth(self):
        print("Total worth: " + str(ExchangeCash.to_usd()+CryptoWorth.calculate_crypto_worth()))


if __name__ == '__main__':
    unittest.main()