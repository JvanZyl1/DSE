"""
Classes
"""


class Lift:

    def __init__(self, L_x, L_y, L_z):
        self.L_x = L_x
        self.L_y = L_y
        self.L_z = L_z
        self.total = self.L_x + self.L_y + self.L_z
    
class Material:

    def __init__(self, tensile_strength, yield_strength, E_modulus, shear_strength, density):
        self.sigma_t = tensile_strength  # Pa
        self.sigma_y = yield_strength  # Pa
        self.E_modulus = E_modulus  # Pa
        self.tau = shear_strength  # Pa
        self.density = density  # kg/m**3

