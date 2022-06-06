

class Employee:

    # Class Variables
    x = 0

    # Instance Variables
    def __init__(self, i):
        self.var = None
        self.i = i

    def method(self, z):
        self.var = 2 * z

emp = Employee(1)