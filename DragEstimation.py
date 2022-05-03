'''Drag Polars as derived for specific concepts by https://www.mdpi.com/2226-4310/6/3/26 '''

from inputs import *
def DragPolar(C_L):
    if VehicleConfig == 'LiftCruise':
        C_D = 0.0438 + 0.0294 * (C_L**2)
    elif VehicleConfig == 'VectorThrust':
        C_D = 0.0163 + 0.058 * (C_L**2)
    return C_D

