import numpy as np
from plot3D import plot3D

def rosen(x):
    """The Rosenbrock function"""
    return np.sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0, axis=0)
#Функция для построения 3D графика,
# вынесена в отдельный файл
plot3D()
from scipy.optimize import minimize
x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
#Метод Нелдера-Мида
res = minimize(rosen, x0, method='nelder-mead', options={'xtol': 1e-8, 'disp':
True})
print(res.x)
"""Optimization terminated successfully.
Current function value: 0.000000
Iterations: 339
Function evaluations: 571
[1. 1. 1. 1. 1.]"""
#Метод Пауэлла
x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(rosen, x0, method='powell',
options={'xtol': 1e-8, 'disp': True})
print(res.x)
"""Optimization terminated successfully.
Current function value: 0.000000
Iterations: 19
Function evaluations: 1622
[1. 1. 1. 1. 1.]"""