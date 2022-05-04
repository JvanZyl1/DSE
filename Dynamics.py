import numpy as np

#angles
a = 0
b = 0
c = 0

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
    Tz = np.matrix([[cos(c), sin(c), 0], [-sin(c), cos(c), 0], [0, 0, 1]])
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
