import unittest
# Here you can add the libraries you use for writing the tests
import numpy as np
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Import ../Parasitedrag_Estimation_Multirotor.py
# Import the file directly as shown
# to import from other folder, do parent folder.(other_folder).file_name
from unused_files.python_scripts import Parasitedrag_Estimation_Multirotor as pm


class MyTestCase(unittest.TestCase):
    '''
    In this class, you make a function for every function of your original code you want to test.
    In every function, you can call the function to test, and assert it equal/almostequal/greaterthan...
    When running this file, it returns if the functions performed as expected. You will see what tests passed or failed.
    '''
    def test_parasite_drag1(self):
        actual_CD0 = 0.644
        test_CD0 = pm.parasite_drag()[0]
        self.assertAlmostEqual(actual_CD0, test_CD0, 2)  # add assertion here

    def test_parasite_drag2(self):
        actual_D_q_tot_x = 0.5057
        test_D_q_tot_x = pm.parasite_drag()[1]
        self.assertAlmostEqual(actual_D_q_tot_x, test_D_q_tot_x, 2)





if __name__ == '__main__':
    unittest.main()

