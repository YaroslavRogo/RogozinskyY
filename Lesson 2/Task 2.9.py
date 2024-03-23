import numpy as np
import matplotlib.pyplot as plt

def func(x, y):
    return (1/4) * np.sin(12*x**2 - y) - np.exp(-((x-5)**2 + (y-2)**2))

x = np.linspace(2, 8, 100)
y = np.linspace(0, 5, 100)
X, Y = np.meshgrid(x, y)

Z = func(X, Y)

# Найти координаты точки минимума
min_idx = np.unravel_index(np.argmin(Z), Z.shape)
min_x = x[min_idx[1]]
min_y = y[min_idx[0]]

# Построить двумерный график функции
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.scatter(min_x, min_y, func(min_x, min_y), color='red', label='Minimum')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.legend()

plt.show()

print(f"Минимум функции находится в точке ({min_x:.1f}, {min_y:.1f})")