import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(-2,3,0.1)
plt.plot(x, 1/((x-0.3)**2+0.01) - 1/((x-0.8)**2+0.04), 'y')
plt.grid(True)
plt.show()