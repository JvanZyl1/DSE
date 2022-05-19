# Imports
from STRUC_Classes import Lift

# Lift assignment
Vertical_max = Lift(8000, 0, 0)
Ground = Lift(0, 0, 0)
Gust = Lift(7000, 1000, 500)

print(Gust.total)
