import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import warnings

mpl.style.use('seaborn-white')
warnings.filterwarnings('ignore')

x0 = (0, 0)  # Начальное предположение
dx = 0.001
x = np.arange(-10, 10, dx)
a, b = 0, 0

def func(t, a, b):
    x, y = t[0], t[1]
    return (x + y)**2 - 2 * x * (y + a) - 2 * y * b + a + b

f0 = lambda t: func(t, a, b)

plt.plot(x, f0((x, 0)))

from scipy.optimize import minimize

result = minimize(f0, x0)

print(result.x)

plt.scatter(result.x[0], result.x[1], c='red')
plt.show()




