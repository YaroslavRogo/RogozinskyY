import matplotlib as mpl
import matplotlib.pyplot as plt
#настройка стилей
plt.style.use('classic')
#Первая визуализация
import numpy as np
x = np.linspace(0, 10, 100)
fig = plt.figure(figsize=(9,5)) #Создание объектаполотна

plt.plot(x, np.sin(x))
y = np.(sin(2*x) * sin(2*x))
plt.show()
#Для проверки поддерживаемых форматов для

# fig.canvas.get_supported_filetypes()
print(fig.canvas.get_supported_filetypes())
#Сохранение рисунков в файл
fig.savefig('my_figure.png')