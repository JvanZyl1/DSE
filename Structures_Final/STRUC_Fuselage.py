
from STRUC_Classes import Boom
import numpy as np
from matplotlib import pyplot as plt

class FuselageLoads:
    def __init__(self, pos_z):
        self.z = pos_z

    def step(self, pos_z_start):
        return np.where(self.z < pos_z_start, 0, 1)

    def Vx(self):
        Vx = np.add(-200 * self.z, 500 * self.step(0.2))
        return Vx

    def Vy(self):
        pass

    def Mx(self):
        pass

    def My(self):
        My = np.add(-2000 * self.z **2, 400 * self.step(0.2) ** 2)
        return My


z_range = np.arange(0, 1, 0.01)
Fuselage = FuselageLoads(z_range)
y = Fuselage.Vx()

plt.plot(z_range, y)
plt.show()
