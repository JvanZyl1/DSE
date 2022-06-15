

class Employee:

    # Class Variables
    x = 0

    # Instance Variables
    def __init__(self, i):
        self.var = None
        self.i = i

    @property
    def method(self):
        self.var = 2 * self.i

emp = Employee(1)

emp.i = 2



"""
print("SHEAR")
for boom in cs.booms:
    print('boom.X, boom.Y', boom.N_B, 'q = ', boom.q, boom.tau_max)
    if abs(boom.tau[0]) <= abs(boom.tau_max[0]) and abs(boom.tau[1]) <= abs(boom.tau_max[1]):
        print('z0 =     OK', 'z1 =     OK', boom.tau, np.around(boom.tau / np.array(boom.tau_max) * 100, 5))
    elif abs(boom.tau[0]) > abs(boom.tau_max[0]) and abs(boom.tau[1]) <= abs(boom.tau_max[1]):
        print('z0 = NOT OK', 'z1 =     OK', boom.tau, np.around(boom.tau / np.array(boom.tau_max) * 100, 5))
    elif abs(boom.tau[0]) <= abs(boom.tau_max[0]) and abs(boom.tau[1]) > abs(boom.tau_max[1]):
        print('z0 =     OK', 'z1 = NOT OK', boom.tau, np.around(boom.tau / np.array(boom.tau_max) * 100, 5))
    else:
        print('z0 = NOT OK', 'z1 = NOT OK', boom.tau, np.around(boom.tau / np.array(boom.tau_max) * 100, 5))

print("\nSTRESS")
for boom in cs.booms:
    print('boom.X, boom.Y', boom.N_B, '           ', '           ', boom.sigma_max)
    if abs(boom.sigma_z[0]) <= abs(boom.sigma_max[0]) and abs(boom.sigma_z[1]) <= abs(boom.sigma_max[1]):
        print(boom.X, boom.Y, 'z0 =     OK', 'z1 =     OK', boom.sigma_z)
    elif abs(boom.sigma_z[0]) > abs(boom.sigma_max[0]) and abs(boom.sigma_z[1]) <= abs(boom.sigma_max[1]):
        print(boom.X, boom.Y, 'z0 = NOT OK', 'z1 =     OK', boom.sigma_z)
    elif abs(boom.sigma_z[0]) <= abs(boom.sigma_max[0]) and abs(boom.sigma_z[1]) > abs(boom.sigma_max[1]):
        print(boom.X, boom.Y, 'z0 =     OK', 'z1 = NOT OK', boom.sigma_z)
    else:
        print(boom.X, boom.Y, 'z0 = NOT OK', 'z1 = NOT OK', boom.sigma_z)


"""