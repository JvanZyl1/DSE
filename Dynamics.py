import numpy as np

#angles
a = 0
b = 0
c = 0

def T_x(a, mat):
    Tx = np.matrix([[1,0,0],[0,np.cos(a),np.sin(a)],[0,-1*np.sin(a),np.cos(a)]])
    mat_rot_x = mat*T_x
    return mat_rot_x

def T_y(b, mat):
    Ty = np.matrix([[np.cos(b),0,-1*np.sin(b)],[0,1,0],[np.sin(b),0,np.cos(b)]])
    mat_rot_y = mat*t_y
    return mat_rot_y
