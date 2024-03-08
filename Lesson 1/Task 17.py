nech = {'a', 'c', 'e', 'g'}
ch = {'b', 'd', 'f', 'h'}

pol = input()
sp = list(pol)
d = sp[0]

if d in nech.intersection(sp):
    for s in sp[1:]:
        a = int(s)
        if a % 2 == 0:
            print('white')
        else:
            print('black')
elif d in ch.intersection(sp):
    for s in sp[1:]:
        a = int(s)
        if a % 2 == 0:
            print('black')
        else:
            print('white')


