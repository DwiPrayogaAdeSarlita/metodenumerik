import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(-2,5,0.1)
plt.plot(x, [math.exp(y) - 5*y**2 for y in x], 'y')
plt.grid(True)
plt.show()