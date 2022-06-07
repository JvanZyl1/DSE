"""
Classes
"""


class Load:
    C_D = 1.
    rho = 1.225

    def __init__(self, L, gustspeed, P, torque):
        self.L = L
        self.D = 0.5 * self.C_D * self.rho * gustspeed ** 2
        self.P = P
        self.T = torque


class Material:

    def __init__(self, tensile_strength, yield_strength, E_modulus, shear_strength, density, G_modulus):
        self.sigma_t = tensile_strength  # Pa
        self.sigma_y = yield_strength  # Pa
        self.E_modulus = E_modulus  # Pa
        self.tau = shear_strength  # Pa
        self.density = density  # kg/m**3
        self.G_modulus = G_modulus







