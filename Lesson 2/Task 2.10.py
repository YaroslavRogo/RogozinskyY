import matplotlib.pyplot as plt
import numpy as np

def func(x, y):
    return np.sin((x) ** 2 + (y) ** 2)/((x) ** 2 + (y) ** 2)

x = np.linspace(-20, 20, 100)
y = np.linspace(-20, 20, 100)
X, Y = np.meshgrid(x, y)
Z = func(X, Y)  # Матрица Z


fig, ax = plt.subplots(1, 1, figsize=(8, 8), subplot_kw={'projection': "3d"})

ax.plot_surface(X, Y, Z / Z.max(), cmap=plt.cm.ocean_r)
ax.view_init(30, 60) #Угол просмотра
plt.show()