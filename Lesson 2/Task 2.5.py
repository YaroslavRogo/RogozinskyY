import numpy as np
import matplotlib.pyplot as plt


counts = [17, 3]
plt.figure(figsize=(5, 5))
plt.pie(counts,
 colors=['royalblue', 'gold'], #цвета долей
 labels=['Dogs', 'Cats'], # подписи
 startangle=120, # начальный угол
 autopct='%.3f%%' # формат вывода значений долей
 )
plt.show()