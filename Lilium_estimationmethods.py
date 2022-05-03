import numpy as np


def wing_sizing(MTOW):
    L = MTOW
    S = L / (CL * 0.5 * rho * Vcruise * Vcruise)
    b = np.sqrt(S) * np.sqrt(10)
    c = np.sqrt(S) / np.sqrt(10)

def battery_sizing():
    T = MTOW

    # Power for hover
    Pmax = np.sqrt((T / Ti) ** 3 / (2 * rho * disk_area))
    print(Pmax)
    # Power for cruise
    Pcruise = 0.1 * Pmax

    # Energy needed for flight stages
    Eto = (2 * Pcruise + 0.5 * Pmax) * 10
    Eclimb = (2 * Pcruise) * 0  # TODO
    Ecruise = Pcruise * 0  # TODO
    Edesc = 0.5 * Pcruise * 0  # TODO
    Eland = (0.5 * Pcruise + 0.5 * Pmax) * 20
    Eres = Pmax * 0  # TODO

    # Total energy needed
    Etot = (Eto + Eclimb + Ecruise + Edesc + Eland + Eres) / 3600

    # Battery sizing
    energy_density = 170  # Wh/kg

def weight_reiteration():
    OEW = Wwing + Wbod + Wemp + Wprop
    MTOW = Wp + Wbat + OEW

Ti = 1.26
rho = 1.225  # kg/m^3
g = 9.81

disk_area = 0.15/2 * np.pi**2 * 36  # Actuator disk area (total)

# First weight estimation
Wbat = 200 * g  # N
OEW = (3174.6 - 771) * (2/7 * 1.5) * g  # N
Wp = 230 * g  # N
MTOW = Wbat + Wp + OEW
L = MTOW
Vcruise = 203 / 3.6  # m/s

# Trade-off between optimal CL and low-wingspan CL
CLmax = 1.4  # ROUGH ESTIMATION
CLopt = 0.52  # FROM DRAG POLAR IN LITERATURE
CL = CLmax

for i in range(100):
    MTOW = Wbat + Wp + OEW
    L = MTOW
    S = L / (CL * 0.5*rho*Vcruise*Vcruise)
    Wwing = 0  # TODO
