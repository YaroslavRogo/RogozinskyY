import matplotlib as mpl
import matplotlib.pyplot as plt
#настройка стилей
plt.style.use('classic')
#Первая визуализация
import numpy as np
x = np.linspace(-10, 10, 1000)
fig = plt.figure(figsize=(8,3)) #Создание объектаполотна
plt.grid(lw=0.5, ls='--')
y = np.sin(2*x)**2 * np.exp((x+2)/10)**2

plt.plot(x, y,  lw = 5.0, color='red', zorder=0)
plt.show()
#Для проверки поддерживаемых форматов для

# fig.canvas.get_supported_filetypes()
print(fig.canvas.get_supported_filetypes())
#Сохранение рисунков в файл
fig.savefig('my_figure.png')