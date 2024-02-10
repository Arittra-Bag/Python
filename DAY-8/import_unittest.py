import unittest
import time
from rand import *

class TestRand(unittest.TestCase):
    
    def test_generate_random_number(self):
        result = generate_random_number(1, 10, 5)
        self.assertEqual(len(result), 5)
        self.assertTrue(all(1 <= x <= 10 for x in result))
        time.sleep(1)
        
    def test_calculate_mean(self):
        result = calculate_mean([1, 2, 3, 4, 5])
        self.assertEqual(result, 3)
        time.sleep(1)
        
    def test_calculate_median(self):
        result = calculate_median([1, 2, 3, 4, 5, 6])
        self.assertEqual(result, 3.5)
        time.sleep(1)
        
    def test_calculate_std_deviation(self):
        result = calculate_std_deviation([1, 2, 3, 4, 5])
        self.assertAlmostEqual(result, 1.41421356, places=5)
        time.sleep(1)
        
if __name__ == '__main__':
    unittest.main()