import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import warnings
mpl.style.use('seaborn-white')
warnings.filterwarnings('ignore')
x0 = float(input()) #начальное предположение
dx = 0.001
x = np.arange(-4,4,dx)
f0 = lambda x:  (x)**2 * (x - 4)**2 * np.exp(-x**2)
plt.plot(x, f0(x))
g0 = lambda x:  - (x)**2 * (x - 4)**2 * np.exp(-x**2)

from scipy.optimize import minimize
result = minimize(g0, x0)
print(result.x)


plt.show()




