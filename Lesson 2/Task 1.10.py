import matplotlib as mpl
import matplotlib.pyplot as plt
#настройка стилей
plt.style.use('classic')
#Первая визуализация
import numpy as np
x = np.linspace(-10, 10, 250)
fig = plt.figure(figsize=(10,5)) #Создание объектаполотна
plt.grid(lw=0.5, ls='--')
y = np.sin(x)
plt.scatter(x, y,
 s=300,
 marker='s',
 c='violet',
 lw=2,
 edgecolor='black',
 hatch='**'
 )



plt.title(
 label='$sin(x)$ with random noise', # Заголовок
 fontsize=20 # Размер шрифта
)
plt.xlabel('x range', fontsize=18)
plt.ylabel('y range', fontsize=18)
plt.tick_params(labelsize=16)

plt.xticks(
    ticks=np.arange(-10, 11, 2) # Нужные значения по оси x
)
plt.yticks(
    ticks=np.arange(-1.5, 2,0.5), labels=['можно', 'написать', 'все', 'что', 'хочется', 'вообще', 'все ='][::-1]
)
plt.plot(x, y,  lw = 5.0, color='red', zorder=0)
plt.show()
#Для проверки поддерживаемых форматов для

# fig.canvas.get_supported_filetypes()
print(fig.canvas.get_supported_filetypes())
#Сохранение рисунков в файл
fig.savefig('my_figure.png')