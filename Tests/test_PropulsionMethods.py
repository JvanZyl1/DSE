import unittest
import numpy as np
from inputs import *
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import PropulsionMethods as pm

class MyTestCase(unittest.TestCase):
    '''
    In this class, you make a function for every function of your original code you want to test.
    In every function, you can call the function to test, and assert it equal/almostequal/greaterthan...
    When running this file, it returns if the functions performed as expected. You will see what tests passed or failed.
    '''

    def test_MOI(self):
        actual_MOI = 105
        test_MOI = pm.MOI_prop(3.5)
        self.assertAlmostEqual(actual_MOI, test_MOI, 0)

    def test_reactiontime(self):
        actual_t_react = 10
        test_t_react = pm.reaction_time(900, 1)
        self.assertEqual(actual_t_react, test_t_react)

    def test_power(self):
        actual_P = 26.91
        test_P = pm.power_from_thrust(10, 1, 1)
        self.assertAlmostEqual(actual_P, test_P, 0)

    def test_inplanerotors(self):
        """Assert whether the function in_plane_rotors calculates a larger RPM,
        a smaller reaction time, and a larger required force for a smaller
        propeller radius."""

        P_cont1, P_total1, t_react1, omega1, chars1 = pm.in_plane_rotors(0.5, 2)
        P_cont2, P_total2, t_react2, omega2, chars2 = pm.in_plane_rotors(2, 2)

        self.assertGreater(omega1, omega2)
        self.assertGreater(t_react2, t_react1)
        self.assertGreater(P_cont1, P_cont2)

    def test_pretilted_gustloads(self):
        """Assert whether the function pre_tilted calculates a higher RPM change,
        reaction time, and total required power for higher gust loads."""
        T_total1, P_total1, t_react1, omega_change1 = pm.pre_tilted(500, 45, MTOW)
        T_total2, P_total2, t_react2, omega_change2 = pm.pre_tilted(1000, 45, MTOW)

        self.assertGreater(omega_change2, omega_change1)
        self.assertGreater(t_react2, t_react1)
        self.assertGreater(P_total2, P_total1)

    def test_pretilted_tiltangles(self):
        """Assert whether the function pre_tilted calculates a higher RPM change,
        reaction time, and total required power for smaller tilt angles."""
        T_total1, P_total1, t_react1, omega_change1 = pm.pre_tilted(100, 45, MTOW)
        T_total2, P_total2, t_react2, omega_change2 = pm.pre_tilted(100, 25, MTOW)

        self.assertGreater(omega_change2, omega_change1)
        self.assertGreater(t_react2, t_react1)
        self.assertGreater(P_total2, P_total1)

    def test_pretilted_rpmchange(self):
        """Assert whether the function pre_tilted chooses the right method of
        disturbance rejection: decreasing the rpm of one motor, or increasing
        the rpm for the other."""
        T_total1, P_total1, t_react1, omega_change1 = pm.pre_tilted(10, 25, MTOW)
        T_total2, P_total2, t_react2, omega_change2 = pm.pre_tilted(1000, 45, MTOW)

        self.assertLess(omega_change1, 0)
        self.assertGreater(omega_change2, 0)


    def test_pretilted_errors(self):
        """Assert that function pre_tilted stops when it is an invalid combination
        of (low) tilt angle and (high) gust load"""
        self.assertRaises(TypeError, pm.pre_tilted(1000, 5, MTOW))




if __name__ == '__main__':
    unittest.main()
