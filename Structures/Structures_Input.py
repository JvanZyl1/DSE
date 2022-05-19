from math import *
import numpy as np
from Structures_Classes import *

# Materials
aluminium = Material(444e6, 400e6, 70e9, 283e6, 2.8e3)
steel = Material(570e6, 240e6, 197e9, 440e6, 8.0e3)
titanium = Material(620e6, 880e6, 113e9, 550e6, 4.43e3)
cf = Material(4274e6, 4274e6, 234e9, 55e6, 691.7)

beam1 = Beam(aluminium, 2, 0.1, 0.001)