import unittest
from old_scripts.Structures_Radius import *

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

class Test_Result_Values(unittest.TestCase):
    def test_internal_load_root(self):
        value_calc = abs((use_loadcase.L - use_beam.weight_engine) / use_beam.n - use_beam.weight)
        value_test = abs(v_beam(use_beam, use_loadcase, 0)[1])
        self.assertAlmostEqual(value_calc, value_test, 1)

    def test_internal_load_tip(self):
        value_calc = abs((use_loadcase.L - use_beam.weight_engine) / use_beam.n)
        value_test = abs(v_beam(use_beam, use_loadcase, use_beam.length)[1])
        self.assertAlmostEqual(value_calc, value_test, 1)

    def test_moment_root(self):
        value_calc = abs((use_loadcase.L - use_beam.weight_engine) * use_beam.length / use_beam.n - use_beam.weight / 2*use_beam.length)
        value_test = abs(m_beam(use_beam, use_loadcase, 0)[0])
        self.assertAlmostEqual(value_calc, value_test, 1)

    def test_deflection_root(self):
        value_calc = 0
        value_test = abs(deflection(use_beam, use_loadcase, use_material, 0))
        self.assertAlmostEqual(value_calc, value_test, 1)

    def test_deflection_tip(self):
        Max = m_beam(use_beam, use_loadcase, 0)[2]
        value_calc = abs(1/(use_material.E_modulus*use_beam.Ixx)*(-Max / 2 * use_beam.length**2 +
            v_beam(use_beam, use_loadcase, 0)[1]/6*use_beam.length ** 3 - use_beam.weight/24 * use_beam.length ** 3))
        value_test = abs(deflection(use_beam, use_loadcase, use_material, use_beam.length))
        self.assertAlmostEqual(value_calc, value_test, 4)

    def test_moment_tip(self):
        value_calc = 0
        value_test = abs(m_beam(use_beam, use_loadcase, use_beam.length)[0])
        self.assertAlmostEqual(value_calc, value_test, 1)

    def test_radius1(self):
        value_calc = use_material.sigma_t
        r_1 = radius(use_beam, use_loadcase, use_material, 0)[0]
        value_test = m_beam(use_beam, use_loadcase, 0)[0] / (use_beam.thickness * r_1**2) + use_loadcase.P / (2*pi*use_beam.thickness * r_1)
        self.assertAlmostEqual(value_calc, value_test, 1)

    def test_radius2(self):
        r_2 = radius(use_beam, use_loadcase, use_material, 0)[1]
        value_test = m_beam(use_beam, use_loadcase, 0)[0] / (use_beam.thickness * r_2 ** 2)
        value_calc = pi ** 2 * use_material.E_modulus * r_2 ** 2 / use_beam.length**2
        self.assertAlmostEqual(value_calc, value_test, 1)

    def test_radius5(self):
        r_6 = radius(use_beam, use_loadcase, use_material, use_beam.length)[5]
        value_calc = use_material.tau
        value_test = v_beam(use_beam, use_loadcase, use_beam.length)[1]/(-pi * use_beam.thickness * r_6**3)
        self.assertAlmostEqual(value_calc, value_test, 1)

Max = m_beam(use_beam, use_loadcase, 0)[0]
value_calc = 1 / (use_material.E_modulus * use_beam.Ixx) * abs(
    -Max / 2 * use_beam.length ** 2 + v_beam(use_beam, use_loadcase, 0)[
        1] / 6 * use_beam.length ** 3 - use_beam.weight / 24 * use_beam.length ** 3)
if __name__ == '__main__':
    unittest.main()
