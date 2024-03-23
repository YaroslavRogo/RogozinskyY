import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import warnings
mpl.style.use('seaborn-white')
warnings.filterwarnings('ignore')
dx = 0.001
x = np.arange(-10, 10, dx)
f0 = lambda x: (x - 0.5)**2
plt.plot(x, f0(x))


from scipy.optimize import minimize
result = minimize(f0, x0=1)
print(result)
fun: 1.3877787807814457e-17
hess_inv: np.array([[1]])
jac: np.array([2.23517418e-08])
message: 'Optimization terminated successfully.'
nfev: 6
nit: 1
njev: 3
status: 0
success: True
x: np.array([0.5])


plt.show()