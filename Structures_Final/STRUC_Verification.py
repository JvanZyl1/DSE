import unittest
from STRUC_Radius import *

class TestNoInput(unittest.TestCase):
    def test_v_beam_NoInput(self):
        self.assertRaises(TypeError, v_beam, 'N/A')

    def test_m_beam_NoInput(self):
        self.assertRaises(TypeError, m_beam, 'N/A')

    def test_deflection_NoInput(self):
        self.assertRaises(TypeError, deflection, 'N/A')

    def test_radius_NoInput_NoInput(self):
        self.assertRaises(TypeError, radius, 'N/A')


"""
class TestType(unittest.TestCase):
    def test_v_beam_TestType(self):
        self.assertRaises(TypeError, v_beam(use_beam, use_loadcase, 1))

    def test_m_beam_TestType(self):
        self.assertRaises(TypeError, m_beam(use_beam, use_loadcase, z))

    def test_deflection_TestType(self):
        self.assertRaises(TypeError, deflection(use_beam, use_loadcase, use_material, z))

    def test_radius_TestType(self):
        self.assertRaises(TypeError, radius(use_beam, use_loadcase, use_material, z))



class TestZeroInput(unittest.TestCase):
    def test_v_beam_Zero(self):
        use_beam.length = 0
        with self.assertRaises(Exception):
            v_beam(use_beam, use_loadcase, 0.1)

    def test_m_beam_Zero(self):
        pass
        # use_beam.length = 0
        # with self.assertRaises(ValueError):
        #    pass

    def test_deflection_Zero(self):
        use_material.E_modulus = 0
        self.assertRaises(ValueError)

    def test_deflection_Zero(self):
        use_material.E_modulus = 0

        self.assertRaises(ValueError)
"""
class TestExtremes(unittest.TestCase):
    def test_v_beam_extremely_long(self):
        use_beam.length = 1e5
        V_y, _ = v_beam(use_beam, use_loadcase, 0.1)
        self.assertLess(abs(V_y), use_loadcase.L + use_beam.weight + use_beam.weight_engine)

    def test_m_beam_extremely_long(self):
        use_beam.length = 1e5
        M_x, M_y, Max, May = m_beam(use_beam, use_loadcase, 0.1)
        self.assertGreater(abs(Max), 10000, "There should be a very large reaction moment")

    def test_deflection_extremely_low_E(self):
        use_material.E_modulus = 0.001
        v = deflection(use_beam, use_loadcase, use_material, use_beam.length-0.1)
        self.assertGreater(abs(v), 10000)


class TestSanity(unittest.TestCase):
    def test_v_beam_sanity(self):
        use_beam.length = 1e5
        V_y, _ = v_beam(use_beam, use_loadcase, 0.1)
        self.assertLess(abs(V_y), use_loadcase.L + use_beam.weight + use_beam.weight_engine)

    def test_m_beam_sanity(self):
        M_x, M_y, Max, May = m_beam(use_beam, use_loadcase, 0.1)
        if use_loadcase.L-use_beam.weight-use_beam.weight_engine > 0:
            self.assertGreater(M_x, 0)
        else:
            self.assertLess(M_x, 0)

    def test_deflection_sanity(self):

        v = deflection(use_beam, use_loadcase, use_material, use_beam.length-0.1)
        self.assertGreater(abs(v), 10000)



if __name__ == '__main__':
    unittest.main()
