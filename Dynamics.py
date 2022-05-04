from distutils.command.config import config
import numpy as np

def read_txt(file):
    '''
    This function reads the file  to create a dictonary

    return: dict - a dictionary of all the constants
    '''
    new_dict = {}
    file_reading = open(str(file), "r") #open the file
    freq = file_reading.readlines()  #read the lines
    for line in freq:
        row = line.split()
        new_dict[str(row[0])] = float(row[1])
    return new_dict

def read_configuration(file):
    '''
    This function reads the file  to create a nested dictionary

    param: file - input txt file to read

    return: w_dict - a nested dictionary
    '''
    w_dict = {}
    file_reading = open(str(file), "r") #open the file
    freq = file_reading.readlines()  #read the lines
    names = []
    for line in freq:
        row = line.split()
        if row[0] not in names:
            names.append(row[0])
    for i in range(len(names)):
        w_dict[names[i]] = {}
    for line in freq:
        row = line.split()
        w_dict[row[0]][row[1]] = float(row[2])
    return w_dict

def T_x(a, mat):
    '''
    This function performs a tranformation around the x-axis

    param: a - x rotation angle [radians]
    param: mat - matrix or vector to rotate

    return mat_rot_x - rotated matrix or vector
    '''
    Tx = np.matrix([[1,0,0],[0,np.cos(a),np.sin(a)],[0,-1*np.sin(a),np.cos(a)]])
    mat_rot_x = mat*Tx
    return mat_rot_x


def T_y(b, mat):
    '''
    This function performs a transformation around the y-axis

    param: b - y rotation angle [radians]
    param: mat - matrix or vector to rotate

    return mat_rot_y - rotated matrix or vector
    '''
    Ty = np.matrix([[np.cos(b),0,-1*np.sin(b)],[0,1,0],[np.sin(b),0,np.cos(b)]])
    mat_rot_y = mat*Ty
    return mat_rot_y

def T_z(c, mat):

    '''
    This function performs a transformation around the z-axis

    param: c - z rotation angle [radians]
    param: mat - matrix or vector to rotate

    return mat_rot_z - rotated matrix or vector
    '''
    Tz = np.matrix([[np.cos(c), np.sin(c), 0], [-np.sin(c), np.cos(c), 0], [0, 0, 1]])
    mat_rot_z = mat*T_z
    return mat_rot_z

def T_zyx(a,b,c,mat):
    '''
    This function performs the z-y-x aerospace standard for transformations

    param: a - x rotation angle [radians]
    param: b - y rotation angle [radians]
    param: c - z rotation angle [radians]
    param: mat - matrix or vector to rotate

    return Tzyx - rotated matrix or vector
    '''
    Tz = T_z(c, mat)
    Tzy = T_y(b, Tz)
    Tzyx = T_x(a, Tzy)
    return Tzyx

def Euler_rot(initial_conds_dict, constant_dict, config_dict, M_aero, F):
    w_vec = np.matrix([[initial_conds_dict["w_x_0"]], [initial_conds_dict["w_y_0"]], [initial_conds_dict["w_z_0"]]])
    #r_cp_cg = np.matrix([[config_dict["x_cg_cp"]], [config_dict["y_cg_cp"]], [config_dict["z_cg_cp"]]])
    I = constant_dict["I_mat"]
    H = np.matmul(I, w_vec)
    w_cross_H = (np.cross(w_vec.T, H.T)).T
    d_arm = np.matrix([[config_dict["quadcopter"]["x_1"], config_dict["quadcopter"]["y_1"], config_dict["quadcopter"]["z_1"]], [config_dict["quadcopter"]["x_2"], config_dict["quadcopter"]["y_2"], config_dict["quadcopter"]["z_2"]], [config_dict["quadcopter"]["x_3"], config_dict["quadcopter"]["y_3"], config_dict["quadcopter"]["z_3"]]])

    return w_cross_H

constant_dict = read_txt("Constants.txt")
initialconds_dict = read_txt("Initial_Conditions.txt")
config_dict = read_configuration("Propulsive_arms.txt")
print(config_dict)
I = np.matrix([[constant_dict['I_xx'], constant_dict['I_xy'], constant_dict['I_xz']],
    [constant_dict['I_yx'], constant_dict['I_yy'], constant_dict['I_yz']],
    [constant_dict['I_zx'], constant_dict['I_zy'], constant_dict['I_zz']]])
constant_dict["I_mat"] = I
M_aero = [[0],[0],[0]]
F = [[0],[0],[0]]
H = Euler_rot(initialconds_dict, constant_dict, config_dict, M_aero, F)
print(H)