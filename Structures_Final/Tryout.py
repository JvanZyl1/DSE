

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