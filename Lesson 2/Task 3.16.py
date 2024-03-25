import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import warnings
mpl.style.use('seaborn-white')
warnings.filterwarnings('ignore')
dx = 0.001
x = np.arange(-10, 10, dx)

f = lambda x: x**2 * ( 1 - 0.1 * (x) **2 )* np.exp(- 0.1 * (x)**2)
fig, ax = plt.subplots()
ax.set(xlabel='x', ylabel='f(x)')
ax.plot(x, f(x))

def get_path(xc):
 global path
 path.append(xc)

x0 = 2.4
path = [x0]
from scipy.optimize import minimize

result = minimize(f, x0=1.5)
x2 = result.x
print(result)

fun: 1.4145952559875395e-12
hess_inv: np.array([[0.50122726]])
jac: np.array([-2.36383401e-06])
message: 'Optimization terminated successfully.'
nfev: 14
nit: 3
njev: 7
status: 0
success: True
x: np.array([-1.18936759e-06])

plt.annotate("", xytext=(2.4, f(2.4)), xy=(x1, f(x1)),
arrowprops=dict(arrowstyle="->"))
plt.annotate("", xytext=(1.5, f(1.5)), xy=(x2, f(x2)),
arrowprops=dict(arrowstyle="->"))
plt.scatter([x1, x2], [f(x1), f(x2)], color = 'tab:red')
plt.scatter([2.4, 1.5], [f(2.4), f(1.5)], color = 'tab:green')
plt.plot(x, f(x), zorder=0)
plt.show()