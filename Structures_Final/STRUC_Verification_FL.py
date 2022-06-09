import unittest
import STRUC_Class_Boom as B
import STRUC_Fuselage as FL
import numpy as np
from math import *
from STRUC_Boomdef import *

class TestBoom(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass Boom')



    def setUp(self):
        self.boom1 = B.Boom([1, 2.0], [2, 3], 0.001, 0.030)
        self.boom2 = B.Boom([2, 1.5], [4, 1], 0.000, 0.003)

    def tearDown(self) -> None:
        pass

    def test_init(self):
        # Check if initiating delivers right amount of items
        self.assertEqual(len(self.boom1.__dict__), 9, 'boom1.__init__ method provided too many/few items.')
        self.assertEqual(len(self.boom2.__dict__), 9, 'boom2.__init__ method provided too many/few items.')

    def test_init_unit(self):
        with self.assertRaises(TypeError):
            B.Boom([1, 2.0], [0, 3], 0.001, 0.030, 0.01)
        with self.assertRaises(TypeError):
            B.Boom([1, 2.0], [0, 3], 0.001)
    """
    def test_properties_cs_np(self):
        with self.assertRaises(expected_exception=IndexError):  # add assertion here
            boom1 = B.Boom(np.array([1, 2]), np.array([2, 3]), 0.001, 0.03)
            boom1.properties_cs([0, 0.5], [0.8, 1.1])
    """
    def test_properties_cs(self):
        self.boom1.properties_cs(4, 2)
        self.boom2.properties_cs(3, 6)
        self.assertEqual(len(self.boom1.__dict__), 11, 'boom1.properties method provided too many/few items.')
        self.assertEqual(len(self.boom2.__dict__), 11, 'boom2.properties method provided too many/few items.')

    def test_weight(self):
        self.boom1.properties_cs(4, 2)
        self.boom2.properties_cs(3, 6)
        self.boom1.weight()

    def test_area_unit(self):
        with self.assertRaises(TypeError):
            self.boom1.area([0])

    def test_Ixx_unit(self):
        self.assertEqual(len(self.boom1.Ixx([0, 0])), 2)
        with self.assertRaises(TypeError):
            self.boom1.Ixx(0)
        with self.assertRaises(IndexError):
            self.boom1.Ixx([0])

    def test_Iyy_unit(self):
        self.assertEqual(len(self.boom2.Iyy([1, 2])), 2)
        with self.assertRaises(TypeError):
            self.boom1.Iyy(1)
        with self.assertRaises(IndexError):
            self.boom1.Iyy([1])

    def test_stress_max(self):
        self.boom1.properties_cs(4, 2)
        self.boom2.properties_cs(3, 6)
        self.assertAlmostEqual(self.boom1.stress_max(400e6, 70e9, 0.1, 0.11, 4000, -2000, 0.03, 0.02, 1), 400e6)
        self.assertAlmostEqual(self.boom1.stress_max(400e6, 70e9, 0.1, 0.11, -4000, -2000, 0.03, 0.02, 1),
                               max(-400e6, -pi ** 2 * 70e9 * (self.boom1.B[1]/pi) / (self.boom1.K * self.boom1.L) ** 2))
        with self.assertRaises(ZeroDivisionError):
            self.boom2.stress_boom(400e6, 70e9, 0.1, 0.11, 4000, -2000, 0, 0.02, 1)
        with self.assertRaises(ZeroDivisionError):
            self.boom2.stress_boom(400e6, 70e9, 0.1, 0.11, 4000, -2000, 0.03, 0, 1)

    def test_stress_boom(self):
        self.assertAlmostEqual(self.boom1.stress_boom(400e6, 70e9, 0.1, 0.11, 4000, -2000, 0.03, 0.02, 1), 195333.3333, 1)
        with self.assertRaises(ZeroDivisionError):
            self.boom2.stress_boom(400e6, 70e9, 0.1, 0.11, 4000, -2000, 0, 0.02, 1)
        with self.assertRaises(ZeroDivisionError):
            self.boom2.stress_boom(400e6, 70e9, 0.1, 0.11, 4000, -2000, 0.03, 0, 1)
        with self.assertRaises(TypeError):
            self.boom1.stress_boom(400e6, 70e9, 0.1, 0.11, 4000, -2000, 0.03, 0.02)
        with self.assertRaises(TypeError):
            self.boom1.stress_boom(400e6, 70e9, 0.1, 0.11, 4000, -2000, 0.03, 0.02, 1, 2)

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass Boom')


# Sanity tests
class testFuselage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass Fuselage')


    @classmethod
    def tearDownClass(cls):
        print('tearDownClass Fuselage')

if __name__ == '__main__':
    unittest.main()
