import unittest
# Here you can add the libraries you use for writing the tests
import numpy as np
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Import ../Parasitedrag_Estimation_Multirotor.py
# Import the file directly as shown, OR
import PowerEstimation as pe

# Here you can add the libraries you use for writing the tests


class MyTestCase(unittest.TestCase):
    '''
    In this class, you make a function for every function of your original code you want to test.
    In every function, you can call the function to test, and assert it equal/almostequal/greaterthan...
    When running this file, it returns if the functions performed as expected. You will see what tests passed or failed.
    '''

    def test_cruise_TOL(self):
        P_cruise, P_TOL = pe.PowerReq(1000, 8, 1, 100/3.6)
        self.assertGreater(P_TOL, P_cruise)

    def test_MTOW(self):
        P_cruise1, P_TOL1 = pe.PowerReq(1000, 8, 1, 100/3.6)
        P_cruise2, P_TOL2 = pe.PowerReq(100, 8, 1, 100/3.6)
        self.assertGreater(P_TOL1, P_TOL2)
        self.assertGreater(P_cruise1, P_cruise2)

    def test_Nprop(self):
        P_cruise1, P_TOL1 = pe.PowerReq(1000, 8, 1, 100/3.6)
        P_cruise2, P_TOL2 = pe.PowerReq(1000, 16, 1, 100/3.6)
        self.assertGreater(P_TOL1, P_TOL2)
        self.assertGreater(P_cruise1, P_cruise2)

    def test_Rprop(self):
        P_cruise1, P_TOL1 = pe.PowerReq(1000, 8, 1, 100/3.6)
        P_cruise2, P_TOL2 = pe.PowerReq(1000, 8, 2, 100/3.6)
        self.assertGreater(P_TOL1, P_TOL2)
        self.assertGreater(P_cruise1, P_cruise2)

    def test_Vcr(self):
        P_cruise1, P_TOL1 = pe.PowerReq(1000, 8, 1, 300/3.6)
        P_cruise2, P_TOL2 = pe.PowerReq(1000, 8, 1, 100/3.6)
        self.assertGreater(P_cruise1, P_cruise2)



if __name__ == '__main__':
    unittest.main()
