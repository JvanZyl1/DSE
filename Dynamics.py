import numpy as np

#angles
a = 0
b = 0
c = 0

def T_x(a, mat):
    Tx = np.matrix([[1,0,0][0,np.cos(a),np.sin(a)],[0,-1*np.sin(a),np.cos(a)]])
    mat_rot_x = mat*T_x
    return mat_rot_x



def T_z(c, mat):
    Tz = np.matrix([[cos(c), sin(c), 0], [-sin(c), cos(c), 0], [0, 0, 1]])
    mat_rot_z = mat*T_z
    return mat_rot_z

print(Tx)