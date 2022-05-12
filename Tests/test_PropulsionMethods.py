import unittest
import numpy as np
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import PropulsionMethods as pm
class MyTestCase(unittest.TestCase):
    '''
    In this class, you make a function for every function of your original code you want to test.
    In every function, you can call the function to test, and assert it equal/almostequal/greaterthan...
    When running this file, it returns if the functions performed as expected. You will see what tests passed or failed.
    '''
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here



if __name__ == '__main__':
    unittest.main()
