import unittest
from CoinWorth import CoinWorth

class Test_TestPrices(unittest.TestCase):
    print("Bitcoin price: " + CoinWorth.bitcoin())

if __name__ == '__main__':
    unittest.main()