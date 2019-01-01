import unittest
from total_worth import CoinWorth
from total_worth import NetWorth 

class Test_TestPrices(unittest.TestCase):
    def test_coin_price(self):
        print("Bitcoin price: " + CoinWorth.get_coin_price("bitcoin"))
        print("Ethereum price: " + CoinWorth.get_coin_price("ethereum"))
        print("Decred price: " + CoinWorth.get_coin_price("decred"))
        print("Bitcoin Cash price: " + CoinWorth.get_coin_price("bitcoin-cash"))
        print("Qash price: " + CoinWorth.get_coin_price("qash"))
        print("Ripple price: " + CoinWorth.get_coin_price("ripple"))

    def test_net_worth_calculator(self):
        print("Total Net Worth: " + str(NetWorth.calculate_net_worth()))

if __name__ == '__main__':
    unittest.main()