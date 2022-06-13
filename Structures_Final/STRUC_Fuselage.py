

import numpy as np
from STRUC_Class_Crosssection import CrossSection
from matplotlib import pyplot as plt

if __name__ == '__main__':
    pass #print('RUN Fuselage\n\n')
else:
    pass #print('class Fuselage imported\n\n')

class Fuselage(CrossSection):


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
            self.weight += cs.weight_booms()
            self.weight += cs.weight_skins()
            cs.weight_cs = cs.weight_booms() + cs.weight_skins()
        return self.weight, cs.weight_cs

    def print_cs(self):
        for cs in self.cross_sections:
            print('-->', cs.Z)

    def plot_cs(self):
        for cs in self.cross_sections:
            plt.plot([cs.Z[0], cs.Z[0]], [-cs.R[0], cs.R[0]], 'r')
            plt.plot(cs.Z, cs.R, 'b')
            plt.plot(cs.Z, -cs.R, 'b')
            for boom in cs.booms:
                plt.plot([cs.Z[0], cs.Z[1]], [boom.Y[0], boom.Y[1]], 'g')
        plt.plot([cs.Z[1], cs.Z[1]], [-cs.R[1], cs.R[1]], 'r')
        plt.xlabel('$z$ [m]')
        plt.ylabel('$y$ [m]')
        plt.grid()
        plt.savefig('fuselage_plot.png')
        plt.show()

    # Loading diagrams: step function
    def step(self, z, z_start):

        if z >= z_start:
            return 1
        return 0  # np.where(self.z < pos_z_start, 0, 1)

    # Loading diagrams functions
    def Vx(self, z):
        z = float(z)
        V_x = 0
        V_x += 450 + 450 * self.step(z, 2.92) + 450*self.step(z, 3.30)
        V_x -= 1350/self.L * z
        return V_x

    def Vy(self, z):
        self.weight_FL()
        z = float(z)
        MTOW = Fuselage.MTOW
        g = Fuselage.g
        n_ult = Fuselage.n_ult
        SF = Fuselage.SF
        V_y = 0
        # FUSELAGE
        for cs in self.cross_sections:
            V_y -= 9.81 * (cs.weight_cs /(cs.Z[1]-cs.Z[0]) * ((z-cs.Z[0])*self.step(z, cs.Z[0])-(z-cs.Z[1])*self.step(z, cs.Z[1])))
        # PASSENGERS
        V_y -= 250* g* self.step(z, 1.57)

        # LUGGAGE
        V_y -= 100 * g * self.step(z, 3.30)

        # BATTERIES
        z_bat = [2.4, 3.2]
        V_y -= 300 /(z_bat[1]-z_bat[0]) * g * ((z-z_bat[0])*self.step(z, z_bat[0])-(z-z_bat[1])*self.step(z, z_bat[1]))
        #print((z - z_bat[0]) * self.step(z, z_bat[0]) - (z - z_bat[1]) * self.step(z, z_bat[1]))
        # Rotors Weight
        V_y -= 13 * g * self.step(z, 0.620) * 2
        V_y -= 13 * g * self.step(z, 2.3) * 4
        V_y -= 13 * g * self.step(z, 2.425) * 2
        # MTOW split up
        V_y -= ((MTOW - self.weight - 250 - 100 - 300 - 13*8) * g)/self.L * z

        # Rotors Lift
        V_y += MTOW * g * self.step(z, 0.620) * 2/8
        V_y += MTOW * g * self.step(z, 2.3) * 4/8
        V_y += MTOW * g * self.step(z, 2.425) * 2/8
        return V_y * n_ult * SF

    def Mx(self, z):

        #self.weight_FL()
        self.Vy(z)
        MTOW = Fuselage.MTOW
        g = Fuselage.g
        n_ult = Fuselage.n_ult
        SF = Fuselage.SF

        M_x = 0

        # FUSELAGE
        for cs in self.cross_sections:
            M_x += cs.weight_cs / (2*(cs.Z[1] - cs.Z[0])) * (
                        (z - cs.Z[0])**2 * self.step(z, cs.Z[0]) - (z - cs.Z[1])**2 * self.step(z, cs.Z[1]))
        # PASSENGERS
        M_x += 250 * g * (z - 1.57) * self.step(z, 1.57)

        # LUGGAGE
        M_x += 100 * g * (z - 3.30) * self.step(z, 3.30)

        # BATTERIES
        z_bat = [2.4, 3.2]
        M_x += 300 / (2*(z_bat[1] - z_bat[0])) * g * (
                    (z - z_bat[0])**2 * self.step(z, z_bat[0]) - (z - z_bat[1])**2 * self.step(z, z_bat[1]))

        # Rotors Weight
        M_x += 13 * g * (z - 0.620) * self.step(z, 0.620) * 2
        M_x += 13 * g * (z - 2.300) * self.step(z, 2.3) * 4
        M_x += 13 * g * (z - 2.425) * self.step(z, 2.425) * 2

        # MTOW split up
        #M_x += ((MTOW-self.weight- 250-100-300-3*13) * g /2) / (2*self.L) * z**2

        # Rotors Lift
        M_x -= MTOW * g * (z - 0.620) * self.step(z, 0.620) * 2 / 8
        M_x -= MTOW * g * (z - 2.300) * self.step(z, 2.300) * 4 / 8
        M_x -= MTOW * g * (z - 2.425) * self.step(z, 2.425) * 2 / 8
        M_x += 5990.985762974158 / (self.L) * z # ASSUMPTION HERE!!!!
        return M_x * n_ult * SF

    def My(self, z):
        self.Vy(z)
        MTOW = Fuselage.MTOW
        g = Fuselage.g
        n_ult = Fuselage.n_ult
        SF = Fuselage.SF

        M_y = 0
        M_y += 450 * z + 450*(z-2.92) * self.step(z, 2.92) + 450*(z-3.3)*self.step(z, 3.30)
        M_y += 0
        M_y -= 1939.50 / (self.L) * z
        return M_y * n_ult * SF

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
            plt.title("Bending moment diagram ")
            plt.xlabel('$z$ [m]'), plt.ylabel('$M_x$ [N m]')
        elif equation.__name__ == "My":
            plt.title("Bending Moment diagram")
            plt.xlabel('$z$ [m]'), plt.ylabel('$M_y$ [N m]')
        elif equation.__name__ == "Vx":
            plt.title("Shear Force diagram")
            plt.xlabel('$z$ [m]'), plt.ylabel('$V_x$ [N]')
        elif equation.__name__ == "Vy":
            plt.title("Shear Force diagram")
            plt.xlabel('$z$ [m]'), plt.ylabel('$V_y$ [N]')
        else:
            raise NameError
        plt.subplots_adjust(0.16)
        if show:
            plt.show()





