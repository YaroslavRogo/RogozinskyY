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

result = minimize(f, x0=x0, tol=1e-2, callback=get_path)
x1 = result.x
print(result)
fun: -3.090047003364168


hess_inv: np.array([[2.91066268]])
jac: np.array([0.00171024])
message: 'Optimization terminated successfully.'
nfev: 12
nit: 3
njev: 6
status: 0
success: True
x: np.array([5.11767426])

plt.scatter([x0], [f(x0)], color = 'tab:green')
plt.plot(path, [f(i) for i in path], '--o', color="black", lw=0.75,
markersize=2)
plt.scatter([x1], [f(x1)], color = 'tab:red')
plt.plot(x, f(x), zorder = 0)
plt.xlim(0, 10)
plt.ylim(-3.5, 2)

plt.show()