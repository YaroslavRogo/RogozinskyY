import matplotlib.pyplot as plt
import numpy as np

# Создаем сетку графиков 2x2
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(8, 6))

x = np.linspace(-2*np.pi, 2*np.pi, 100)

ax[0, 0].plot(x, np.sin(x))
ax[0, 0].set_title('sin(x)')

ax[0, 1].plot(x, np.sin(x/2))
ax[0, 1].set_title('sin(x/2)')

ax[1, 0].plot(x, np.cos(x))
ax[1, 0].set_title('cos(x)')

ax[1, 1].plot(x, np.cos(x/2))
ax[1, 1].set_title('cos(x/2)')

fig.suptitle('Графики функций')

fig.tight_layout()

plt.show()