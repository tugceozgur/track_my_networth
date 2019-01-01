import unittest
from CoinWorth import CoinWorth

class Test_TestPrices(unittest.TestCase):
    print("Bitcoin price: " + CoinWorth.bitcoin())
    print("Ethereum price: " + CoinWorth.ethereum())
    print("Decred price: " + CoinWorth.decred())
    print("Bitcoin Cash price: " + CoinWorth.bitcoin_cash())
    print("Qash price: " + CoinWorth.qash())
    print("Ripple price: " + CoinWorth.ripple())


if __name__ == '__main__':
    unittest.main()