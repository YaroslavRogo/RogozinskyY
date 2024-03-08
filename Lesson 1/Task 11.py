
melt = {'Sn':232, 'Zn':420, 'Fe':1539, 'Ni':1455, 'Si':1415, 'Be':1287}
print ('Введите элементы для сравнения ')
e1 = input()
e2 = input()
el1 = melt.get(e1)
el2 = melt.get(e2)
el1 = int(el1)
el2 = int(el2)
a = (el1 - el2)
print(abs(a))


