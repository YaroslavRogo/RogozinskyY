import numpy as np
import numpy as np
import matplotlib.pyplot as plt

# Генерация данных
N = 150
r = np.linspace(0, 4, N)
theta = np.linspace(0, 2*np.pi, N)

sizes = r * 50

# Цвет точек в зависимости от полярного угла
colors = theta

plt.figure(figsize=(6, 6))
plt.axes(projection='polar')

plt.scatter(theta, r,
 s=400*r**2,
 c=theta,
 cmap='hsv',
 alpha=0.8
 )

# Отображение графика
plt.show()