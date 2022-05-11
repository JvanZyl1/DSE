import unittest
# Here you can add the libraries you use for writing the tests
import numpy as np
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Import ../Parasitedrag_Estimation_Multirotor.py
# Import the file directly as shown
# to import from other folder, do parent folder.(other_folder).file_name
import DragEstimation as de


class MyTestCase(unittest.TestCase):
    '''
    In this class, you make a function for every function of your original code you want to test.
    In every function, you can call the function to test, and assert it equal/almostequal/greaterthan...
    When running this file, it returns if the functions performed as expected. You will see what tests passed or failed.
    '''
    def test_DragPolar(self):
        '''Lift drag estimations for lift&cruise and VectorThrust.'''
        actual_C_L = 0.05115
        test_C_L = de.DragPolar(0.5)
        self.assertAlmostEqual(actual_C_L, test_C_L, 2)

    def test_RC_AoAandThrust(self):
        test_alpha = de.RC_AoAandThrust(10, 0.5057, 1.225, 600, 9.81)[0]
        test_Treq = de.RC_AoAandThrust(10, 0.5057, 1.225, 600, 9.81)[1]

        actual_alpha = 0.00526
        actual_Treq = 600.79897
        self.assertAlmostEqual(actual_alpha, test_alpha, 2)
        self.assertAlmostEqual(actual_Treq, test_Treq, 2)

    def test_drag_parasitic_fuselage(self):
        test_drag_fuselage = de.drag_parasitic_fuselage(10)
        actual_drag_fuselage = 30.9713
        self.assertAlmostEqual(actual_drag_fuselage, test_drag_fuselage, 2)
        
    def test_FOR_AOA(self):
        test_aoa = de.FOR_AOA(10, 3)
        actual_aoa = 0.1507
        self.assertAlmostEqual(actual_aoa, test_aoa, 2)
    
    def test_V_ind_FOR_non_dim(self):
        test_vind = de.V_ind_FOR_non_dim(10, 3)
        actual_vind = 0.09985
        self.assertAlmostEqual(actual_vind, test_vind, 2)

    def test_V_ind_FOR(self):
        test_vindd = de.V_ind_FOR(10, 800, gamma=3)
        actual_vindd = 1.2724
        self.assertAlmostEqual(actual_vindd, test_vindd, 2)

    def test_Windforces_RC(rho, Vx, Vy, Vz, V_ind, Vw_x, Vw_y, Vw_z):
        test_Fw_x = de.Windforces_RC(1.225,20, 0, 3, 2, 15, 15, 15)[0]
        test_Fw_y = de.Windforces_RC(1.225,20, 0, 3, 2, 15, 15, 15)[1]
        actual_Fw_x = 7
        actual_Fw_x = 7
        print(test_Fw_x, test_Fw_y)






if __name__ == '__main__':
    unittest.main()
