class material:

    def __init__(self, tensile_strength, yield_strength, E_modulus, shear_strength, weight):
        self.sigma_t = tensile_strength #Pa
        self.sigma_y = yield_strength #Pa
        self.E_modulus = E_modulus #Pa
        self.tau = shear_strength #Pa
        self.weight = weight #kg/m**3

#Materials
aluminium = material( 444e6,  400e6,  70e9, 283e6, 2.8e3)
steel =     material( 570e6,  240e6, 197e9, 440e6, 8.0e3)
titanium =  material( 620e6,  880e6, 113e9, 550e6, 4.43e3)
cf =        material(4274e6, 4274e6, 234e9, 55e6, 691.7)


#print(aluminium.sigma_t)