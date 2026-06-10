import unittest
import os
import csv
from main import STOCK_PRICES, calculate_portfolio_value

class TestStockPortfolioTracker(unittest.TestCase):
    
    def test_stock_prices_dict(self):
        # Verify the key stocks are in the dictionary
        self.assertIn("AAPL", STOCK_PRICES)
        self.assertIn("TSLA", STOCK_PRICES)
        self.assertEqual(STOCK_PRICES["AAPL"], 180.00)
        self.assertEqual(STOCK_PRICES["TSLA"], 250.00)

    def test_calculate_portfolio_value(self):
        # Create a sample portfolio
        portfolio = {
            "AAPL": 10,  # 10 * 180 = 1800
            "TSLA": 5    # 5 * 250 = 1250
        }
        
        details, grand_total = calculate_portfolio_value(portfolio)
        
        # Total expected value: 1800 + 1250 = 3050.0
        self.assertEqual(grand_total, 3050.0)
        
        # Verify detailed stock structures
        self.assertEqual(details["AAPL"]["quantity"], 10)
        self.assertEqual(details["AAPL"]["price"], 180.00)
        self.assertEqual(details["AAPL"]["total_value"], 1800.00)
        
        self.assertEqual(details["TSLA"]["quantity"], 5)
        self.assertEqual(details["TSLA"]["price"], 250.00)
        self.assertEqual(details["TSLA"]["total_value"], 1250.00)

if __name__ == "__main__":
    unittest.main()
