import unittest
import Structures_loads_Ehang as test
from Materials import *

class MyTestCase(unittest.TestCase):
    def test_v_beam(self):
        actual_Vz = -1854.812
        test_Vz = test.v_beam(3.6*9.81, 52*9.81 / 4, 2, 1, 8000)
        self.assertAlmostEqual(actual_Vz, test_Vz, 2)  # add assertion here

    def test_m_beam1(self):
        actual_Mz = 1863.641
        test_Mz = test.m_beam(3.6*9.81, 52*9.81 / 4, 2, 1, 8000)
        self.assertAlmostEqual(actual_Mz, test_Mz, 2)

    def test_m_beam2(self):
        test_Mz_d = test.m_beam(test.W_beam, test.W_engine, test.d, test.d, test.L)
        self.assertEqual(test_Mz_d, 0)

    def test_stress_beam1(self):
        actual_sigma_x = 2.75686538e+08
        test_sigma_x = test.stress_beam(3.6*9.81, 52*9.81 / 4, 2, 1, 8000, 0.13, 0.5e-3*0.13**3)[0]
        self.assertAlmostEqual(actual_sigma_x, test_sigma_x, -1)

    def test_stress_beam2(self):
        test_sigma_x = test.stress_beam(test.W_beam, test.W_engine, test.d, 0, test.L, test.r, test.Ixx)
        if test.L >= test.W_beam + test.W_engine:
            self.assertGreaterEqual(test_sigma_x, 0, "More lift then weight ")
        else:
            self.assertLess(test_sigma_x, 0)
    def test_shear_beam(self):
        actual_tau = 5.37464722e+08
        test_tau = test.shear_beam(3.6*9.81, 52*9.81 / 4, 2, 1, 8000, 0.13, 0.5e-3, 0.13)[0]
        self.assertAlmostEqual(actual_tau, test_tau, -1)

    def test_weight_beam(self):
        actual_weight = 3.6184864184047236
        test_weight = test.weight_beam(titanium, 0.5e-3, 0.13, 2)
        self.assertAlmostEqual(actual_weight, test_weight, 2)


if __name__ == '__main__':
    unittest.main()
