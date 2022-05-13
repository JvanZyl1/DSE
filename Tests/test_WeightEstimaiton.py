import unittest
# Here you can add the libraries you use for writing the tests
import numpy as np
# Import ../Parasitedrag_Estimation_Multirotor.py
# Import the file directly as shown, OR
# to import from other folder, do parent folder.(other_folder).file_name
from inputs import *
from MassEstimation import * 
from PowerEstimation import *
from CostEstimation import *
# Here you can add the libraries you use for writing the tests

P_cruise, P_TOL = PowerReq(MTOW, N_prop, R_prop, V_cr)
BatWt, BatWts, E_total = BatteryMassFun(R, R_div, V_cr, V_TO, h_TO, eta_E, P_TOL, P_cruise, nu_discharge)
PropWt, PropWts = PropGroupMassFun(N_prop, R_prop, B_prop, P_TOL)
FuseWt, FuseWts = FuselageGroupMassFun(MTOW, W_PL, l_t, V_cr, D, l, S_nac, N_nac)
Weights = np.vstack((BatWts,PropWts,FuseWts))
MTOW = np.sum([PropWt, FuseWt, BatWt, W_PL])
message = 'Epic FAIL'

class MyTestCase(unittest.TestCase):
    '''
    In this class, you make a function for every function of your original code you want to test.
    In every function, you can call the function to test, and assert it equal/almostequal/greaterthan...
    When running this file, it returns if the functions performed as expected. You will see what tests passed or failed.
    '''
    def test_something(self):

        self.assertGreater(MTOW, 0, message)
        self.assertGreater(MTOW, 0, message)

if __name__ == '__main__':
    unittest.main()
