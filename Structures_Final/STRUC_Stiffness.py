from STRUC_Inputs import *
from math import *
import numpy as np


def deflection_y(beam, material):
    d = 1/(material.E_modulus*beam.Iyy)
    return d

print(deflection_y(beam2, aluminium))

def deflection_x(beam, load):
    pass


def deflection_theta(beam, load):
    pass