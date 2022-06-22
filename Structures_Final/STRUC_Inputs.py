# Imports
from STRUC_Classes import Load, Material
from STRUC_Design import Beam, Gear, Propeller
import numpy as np

# Values
MTOW = 700
g = 9.81
SF = 1.5
n_ult = 2.0

# Lift assignment
Vertical_max = Load(MTOW * g * n_ult * SF, 0, 0, 0)
Landing = Load(0, 0, MTOW * g * n_ult * SF, 0)
Ground = Load(0, 0, 0, 0)
Gust = Load(MTOW * g * n_ult * SF, 121, 0, 0)

# Materials (tens, yield, E, tau, density, G)
aluminium = Material(444e6, 400e6, 70e9, 283e6, 2.8e3, 26.9e9)
steel = Material(570e6, 240e6, 197e9, 440e6, 8.0e3, 0)
titanium = Material(620e6, 880e6, 113e9, 550e6, 4.43e3, 0)
carbon = Material(4274e6, 4274e6, 234e9, 55e6, 691.7, 0)

# Beams (Material,
beam1 = Beam(aluminium, 1.836, 0.08, 52, 0.0025)
beam2 = Beam(aluminium, 1.486, 0.08, 52, 0.0025)
beam3 = Beam(aluminium, 1.6, 0.20, 52, 0.00060)
beam4 = Beam(aluminium, 5.0, 0.08, 52, 0.0050)
beam5 = Beam(aluminium, 2.4, 0.08, 52, 0.0020)
beam6 = Beam(aluminium, 2.0, 0.20, 52, 0.0050)
beam7 = Beam(aluminium, 2.0, 0.20, 52, 0.0050)
beam8 = Beam(aluminium, 2.0, 0.20, 52, 0.0050)

# Gear
#gear1 = Gear(aluminium, 0.4, 0.06, 0.003)

#propeller1 = Propeller(aluminium, 0.2, 0, 0, 0.001)

# Input  beam
use_material = aluminium
use_beam = beam2
use_loadcase = Vertical_max
