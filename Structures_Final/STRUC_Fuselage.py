

import numpy as np
from matplotlib import pyplot as plt

class FuselageLoads:
    def __init__(self, pos_z):
        self.z = pos_z

    def step(self, pos_z_start):
        if self.z >= pos_z_start:
            return 1
        return 0  # np.where(self.z < pos_z_start, 0, 1)

    def Vx(self):
        Vx = -200 * self.z + 500 * self.step(0.2)
        return Vx

    def Vy(self):
        Vy = -100 * self.z + 500 * self.step(0.3)
        return Vy

    def Mx(self):
        Mx = -2000 * self.z ** 2 + 400 * self.step(0.2) ** 2
        return Mx

    def My(self):
        My = -2000 * self.z ** 2 + 400 * self.step(0.2) ** 2
        return My


z_val = 0.3
Fuselage = FuselageLoads(z_val)
y = Fuselage.Mx()
print(y)