import numpy as np

def read_constants():
    '''
    This function reads the file Constants.txt to create the constants dictionary

    return: constant_dict - a dictionary of all the constants
    '''
    constant_dict = {}
    file = "Constants.txt"
    file_reading = open(str(file), "r") #open the file
    freq = file_reading.readlines()  #read the lines
    for line in freq:
        row = line.split()
        constant_dict[str(row[0])] = float(row[1])
    return constant_dict

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


constant_dict = read_constants()
I = np.matrix([[constant_dict['I_xx'], constant_dict['I_xy'], constant_dict['I_xz']],
    [constant_dict['I_yx'], constant_dict['I_yy'], constant_dict['I_yz']],
    [constant_dict['I_zx'], constant_dict['I_zy'], constant_dict['I_zz']]])

