# Imports
from STRUC_Classes import Lift, Material
from STRUC_Design import Beam
# Lift assignment
Vertical_max = Lift(8000, 0, 0)
Ground = Lift(0, 0, 0)
Gust1 = Lift(8000, 0, 500)
Gust2 = Lift(8000, 500, 0)
Gust3 = Lift(8000, 354, 354)
Gust4 = Lift(8000, -354, 354)
Gust5 = Lift(8000, 354, -354)



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