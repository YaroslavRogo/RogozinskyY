import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5*np.pi, 5*np.pi, np.power(10,7))
y1 = np.random.normal(loc=-10, scale=7, size=len(x))
y2 = np.random.normal(loc=10, scale=5, size=len(x))
y3 = np.random.normal(loc=25, scale=10, size=int(len(x)*1.5))

y = np.concatenate([y1, y2, y3])

plt.hist(y, bins=100)
plt.show()