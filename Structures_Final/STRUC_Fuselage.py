

import numpy as np
from STRUC_Class_Crosssection import CrossSection
from matplotlib import pyplot as plt

if __name__ == '__main__':
    pass #print('RUN Fuselage\n\n')
else:
    pass #print('class Fuselage imported\n\n')

class Fuselage(CrossSection):
    sigma_y = 400e6
    E = 70e9
    dz = 0.01
    MTOW = 950
    g = 9.81
    n_ult = 2
    SF = 1.5

    def __init__(self, length, pos_z=None, radius=None, cross_sections=None):
        self.L = length
        self.cross_sections = []
        CrossSection.__init__(self, pos_z, radius)
        if cross_sections is None:
            self.cross_sections = []
        else:
            self.cross_sections = cross_sections


    #Cross-Sections Management
    def add_cs(self, cs_lst):
        for cs in cs_lst:
            if cs not in self.cross_sections:
                cs.N_CS = cs_lst.index(cs)
                self.cross_sections.append(cs)

    def remove_cs(self, cs):
        self.booms.remove(cs)

    def weight_FL(self):  # Checked
        self.weight = 0
        for cs in self.cross_sections:
            cs.weight = cs.weight_booms() + cs.weight_skins()
            self.weight += cs.weight_booms()
            self.weight += cs.weight_skins()

    def print_cs(self):
        for cs in self.cross_sections:
            print('-->', cs.Z)

    def plot_cs(self):
        for cs in self.cross_sections:
            plt.plot(cs.Z, cs.R, 'b')
            plt.plot(cs.Z, -cs.R, 'b')
        plt.show()

    # Loading diagrams: step function
    def step(self, z, z_start):
        if z >= z_start:
            return 1
        return 0  # np.where(self.z < pos_z_start, 0, 1)

    # Loading diagrams functions
    def Vx(self, z):
        Vx = -200 * z + 500 * self.step(z, 0.2)
        return Vx

    def Vy(self, z):
        MTOW = Fuselage.MTOW
        g = Fuselage.g
        n_ult = Fuselage.n_ult
        SF = Fuselage.SF
        self.weight_FL()
        V_y = 0
        c = []

        # FUSELAGE
        for cs in self.cross_sections:
            V_y -= cs.weight/(cs.Z[1]-cs.Z[0]) * ((z-cs.Z[0])*self.step(z, cs.Z[0])-(z-cs.Z[1])*self.step(z, cs.Z[1]))

        # FRONTAL PROPULSION
        V_y += MTOW * g * n_ult * SF / 4 * self.step(z, 0.25)

        # LOWER AFT PROPULSION
        V_y += MTOW * g * n_ult * SF / 4 * self.step(z, 1.35)

        # UPPER AFT PROPULSION
        V_y += MTOW * g * n_ult * SF / 2 * self.step(z, 1.25)

        # PASSENGERS
        V_y -= 250 * g * n_ult * SF * self.step(z, 0.75)

        # LUGGAGE
        V_y -= 100 * g * n_ult * SF * self.step(z, 1.55)

        # BATTERIES
        z_bat = [1.4, 1.7]
        V_y -= 300 /(z_bat[1]-z_bat[0]) * g * n_ult * SF * ((z-z_bat[0])*self.step(z, z_bat[0])-(z-z_bat[1])*self.step(z, z_bat[1]))

        return V_y

    def Mx(self, z):
        Mx = -2000 * z ** 2 + 400 * self.step(z, 0.2) ** 2
        return Mx

    def My(self, z):
        My = -2000 * z ** 2 + 4000 * self.step(z, 0.2) ** 2
        return My

    def stress_FL(self):
        for cs in self.cross_sections:
            cs.stress_CS(Fuselage.sigma_y, Fuselage.E, self.Mx(cs.Z[0]), self.My(cs.Z[0]), 0)
            cs.stress_CS(Fuselage.sigma_y, Fuselage.E, self.Mx(cs.Z[1]), self.My(cs.Z[1]), 1)

    def shear_FL(self):
        self.stress_FL()
        for cs in self.cross_sections:
            cs.shear_CS(self.Vx(cs.Z[0]), self.Vy(cs.Z[1]), 0)
            cs.shear_CS(self.Vx(cs.Z[1]), self.Vy(cs.Z[1]), 1)


    def plot_loads(self, equation, show=False):
        #print(equation.__name__)

        z_range = np.arange(0, self.L + Fuselage.dz, Fuselage.dz)
        result = []
        for z_val in z_range:
            result.append(equation(z_val))
        plt.plot(z_range, result)

        if equation.__name__ == "Mx":
            plt.title("Moment diagram")
            plt.xlabel('$z$ [m]'), plt.ylabel('$M_x$ [N m]')
        elif equation.__name__ == "My":
            plt.title("Moment diagram")
            plt.xlabel('$z$ [m]'), plt.ylabel('$M_y$ [N m]')
        elif equation.__name__ == "Vx":
            plt.title("Internal load diagram")
            plt.xlabel('$z$ [m]'), plt.ylabel('$V_x$ [N]')
        elif equation.__name__ == "Vy":
            plt.title("Internal load diagram")
            plt.xlabel('$z$ [m]'), plt.ylabel('$V_y$ [N]')
        else:
            raise NameError

        if show:
            plt.show()





