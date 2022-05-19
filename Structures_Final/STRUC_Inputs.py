# Imports
from STRUC_Classes import Lift, Material

# Lift assignment
Vertical_max = Lift(8000, 0, 0)
Ground = Lift(0, 0, 0)
Gust = Lift(7000, 1000, 500)

# Materials
aluminium = Material(444e6, 400e6, 70e9, 283e6, 2.8e3)
steel = Material(570e6, 240e6, 197e9, 440e6, 8.0e3)
titanium = Material(620e6, 880e6, 113e9, 550e6, 4.43e3)
carbon = Material(4274e6, 4274e6, 234e9, 55e6, 691.7)

print(Gust.total)
