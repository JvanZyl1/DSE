import numpy as np
from matplotlib import pyplot as plt

z = np.arange(0, 10, 0.1)
x = 0.03 * (z-9) ** 2 + 3

plt.plot(z, x)
plt.show()
