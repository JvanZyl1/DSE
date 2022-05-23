from STRUC_Inputs import *

"""
DSE: Structures
Beam Loading and Stresses
"""

# Imports

from STRUC_Inputs import *
from math import *
import numpy as np


def axes(beam):
    dx, dy, dz = 0.005, 0.005, 0.01
    z_ax = np.arange(0, beam.length + dz, dz)  # Beam span Direction
    x_ax = np.arange(-beam.radius, beam.radius, dx)  # Vertical Direction
    y_ax = np.arange(-beam.radius, beam.radius, dy)
    return x_ax, y_ax, z_ax


x, y, z = axes(use_beam)


# Internal Load Function along z-axis
def v_beam(beam, load, pos_z):
    Vy = beam.weight + beam.weight_engine - load.L / n - beam.weight * pos_z / beam.length
    Vx = -load.D
    return Vx, Vy


def m_beam(beam, load, pos_z):
    M_ax = (beam.weight / 2 + beam.weight_engine - load.L / n) * beam.length
    Mx = (beam.weight + beam.weight_engine - load.L / n) * pos_z - beam.weight * pos_z ** 2 / (2 * beam.length) - M_ax
    M_ay = beam.length * load.D * beam.radius * 2 * beam.length
    My = M_ay - M_ay * pos_z / beam.length + load.T
    return Mx, My

def stress(beam, load, material, pos_z):
    tensile_strength = material.sigma_t
    buckling_strength = -(pi ** 2 * material.E_modulus / (beam.K * beam.length / beam.radius) ** 2 + 1.2 * pi ** 2 * (
            material.E_modulus / material.G_modulus))
    M_x, M_y = m_beam(beam, load, pos_z)
    r1 = (M_y + sqrt(M_y ** 2 + 4 * 2 * pi * beam.thickness * tensile_strength * 2*pi * load.P)) / (4*pi*beam.thickness*tensile_strength)
    r2 = (pi**3 * material.E_modulus*2 * beam.thickness) / (-M_y*beam.K**2*beam.length**2 + 2 * pi * load.P * beam.K**2 * beam.length**2)

    #print(tensile_strength, buckling_strength)
    print(r1, r2)

for i in np.arange(0, 2.1, 0.1):
    #print(m_beam(use_beam, use_loadcase, i))
    stress(use_beam, use_loadcase, use_material, i)



"""
# Bending stress along x- and z-axis
def stress_beam(beam, load, pos_z):
    x, y, z = axes(beam)
    sigma_L_z = load.P / (2 * pi * beam.radius * beam.thickness)
    sigma_bend_y = (m_beam(beam, load, pos_z)[1] / beam.Ixx) * y
    sigma_bend_x = (m_beam(beam, load, pos_z)[0] / beam.Iyy) * x
    sigma_z_y_max = np.amax(np.add(sigma_bend_y, sigma_L_z * np.ones(np.shape(sigma_bend_y))))
    sigma_z_y_min = np.amin(np.add(sigma_bend_y, sigma_L_z * np.ones(np.shape(sigma_bend_y))))
    sigma_z_x_max = np.amax(np.add(sigma_bend_x, sigma_L_z * np.ones(np.shape(sigma_bend_x))))
    sigma_z_x_min = np.amin(np.add(sigma_bend_x, sigma_L_z * np.ones(np.shape(sigma_bend_x))))
    return max(sigma_z_x_max, sigma_z_y_max), min(sigma_z_x_min, sigma_z_y_min)


def sigma_buckling(beam, material):
    sigma_b = -(pi ** 2 * material.E_modulus / (beam.K * beam.length / beam.radius) ** 2 + 1.2 * pi ** 2 * (
            material.E_modulus / material.G_modulus))
    return sigma_b


def shear_beam(beam, load, pos_z):
    x, y, z = axes(beam)
    Vx = v_beam(beam, load, pos_z)[0]
    Vy = v_beam(beam, load, pos_z)[1]
    shear_x_max = np.amax(Vx / (-pi * beam.thickness * beam.radius ** 4) * y)
    shear_y_max = np.amax(Vy / (-pi * beam.thickness * beam.radius ** 4) * x)
    shear_x_min = np.amin(Vx / (-pi * beam.thickness * beam.radius ** 4) * y)
    shear_y_min = np.amin(Vy / (-pi * beam.thickness * beam.radius ** 4) * x)
    return min(shear_x_min, shear_y_min), max(shear_x_max, shear_y_max)


def iterate_radius(beam, load, material, pos_z):
    stress_t, stress_c = stress_beam(beam, load, pos_z)
    shear_min, shear_max = shear_beam(beam, load, pos_z)

    #print(stress_beam(beam, load, pos_z))
    #print(shear_beam(beam, load, pos_z))

    '''
    if material.sigma_t / 1.25 > stress_t:
        print("tensile =   OK  ", round(material.sigma_t, 0) / 1.25, stress_t)
    if sigma_buckling(beam, material) / 1.25 < stress_c:
        print("Buckling =  OK  ", round(sigma_buckling(beam, material), 0) / 1.25, stress_c)
    if abs(shear_min) < material.tau / 1.25:
        print("Shear_min = OK  ", round(abs(shear_min),0), material.tau / 1.25)
    if abs(shear_max) < material.tau / 1.25:
        print("Shear_max = OK  ", round(abs(shear_max), 0), material.tau / 1.25)
    '''

    if material.sigma_t / 1.25 > stress_t and sigma_buckling(beam, material) / 1.25 < stress_c and \
            abs(shear_min) < material.tau and abs(shear_max) < material.tau / 1.25:
        while material.sigma_t / 1.25 > stress_t and sigma_buckling(beam, material) / 1.25 < stress_c and \
                abs(shear_min) < material.tau and abs(shear_max) < material.tau / 1.25:
            stress_t, stress_c = stress_beam(beam, load, pos_z)
            shear_min, shear_max = shear_beam(beam, load, pos_z)
            print(beam.radius)
            beam.radius -= 0.001
        return beam.radius
    else:
        beam.radius += 0.001
        return iterate_radius(beam, load, material, pos_z)

iterate_radius(use_beam, use_loadcase, use_material, 0.9)
"""
