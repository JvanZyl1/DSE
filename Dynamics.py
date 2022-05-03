import numpy as np

#angles
a = 0
b = 0
c = 0

Tx = np.matrix([[1,0,0][0,np.cos(a),np.sin(a)],[0,-1*np.sin(a),np.cos(a)]])

print(Tx)