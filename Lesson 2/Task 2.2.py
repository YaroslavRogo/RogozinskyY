import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('classic')

x = np.linspace(-10, 10, 250)

#
def f(x):
    return np.sin(x)

y = f(x) + np.random.normal(0, 0.2, len(x))

# Создание объекта полотна
fig = plt.figure(figsize=(10, 5))

# Рассеянный график с зашумленными точками
plt.scatter(x, y, s=300, marker='s', c='violet', lw=2, edgecolor='black', hatch='**')

# Линейный график исходной функции
plt.plot(x, f(x), lw=5.0, color='white', zorder=0)

# Настройка осей и меток
plt.grid(lw=0.5, ls='--')
plt.title(label='$sin(x)$ График настроения', fontsize=20)
plt.xlabel('x range', fontsize=18)
plt.ylabel('y range', fontsize=18)
plt.tick_params(labelsize=16)
plt.xticks(ticks=np.arange(-10, 11, 2))
plt.yticks(ticks=np.arange(-1.5, 2, 0.5), labels=['Замечательное настроение', 'хорошее настроение', 'нормальное настроение', 'плохое настроение', 'ещё более плохое настроение', 'депрессия', '0'][::-1])

# Отображение графика
plt.show()

# Сохранение графика в файл
fig.savefig('my_figure.png')

# Вывод поддерживаемых форматов сохранения
print(fig.canvas.get_supported_filetypes())