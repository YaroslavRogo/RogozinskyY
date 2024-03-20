import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-whitegrid')

#Простая гистограмма
data = np.random.randn(1000)
plt.hist(data)
plt.show()
