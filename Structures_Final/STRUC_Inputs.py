# Imports
from STRUC_Classes import Load, Material
from STRUC_Design import Beam

# Values
SF = 1.25

# Lift assignment
Vertical_max = Load(8000, 0, 0, 1000)
Ground = Load(0, 0, 0, 0)
Gust = Load(8000, 21, 5000, 1000)



# Materials
aluminium = Material(444e6, 400e6, 70e9, 283e6, 2.8e3)
steel = Material(570e6, 240e6, 197e9, 440e6, 8.0e3)
titanium = Material(620e6, 880e6, 113e9, 550e6, 4.43e3)
carbon = Material(4274e6, 4274e6, 234e9, 55e6, 691.7)

n = 6

# Beams
beam1 = Beam(5, 1.2, 0.08, 52 / n, 0.0035)
beam2 = Beam(5, 1.4, 0.08, 52 / n, 0.0035)  # The weight, radius and thickness should be iterated and is not correct here!!!!!!
beam3 = Beam(5, 2.0, 0.08, 52 / n, 0.0035)
beam4 = Beam(5, 2.4, 0.08, 52 / n, 0.0035)