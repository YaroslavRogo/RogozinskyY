import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 40)
y = np.sin(x) + np.tan(2 * (x - 2))
yerr = np.random.sample(40) * 2 - 1
plt.figure(figsize=(10, 5))
plt.errorbar(x, y,
 yerr=yerr,
 ecolor='forestgreen', # цвет
 capsize=10, # ширина
 elinewidth=1.5 # толщина
 )
plt.show()
