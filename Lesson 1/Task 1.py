print ('Введите число от 1 до 32')
room = int(input())
if room <= 16:
    if room  >= 9 and room  <= 16:
       print('2 подъезд')
    else:
        print('1 подъезд')
elif room >= 17:
    if 25 <= room + 8 <= 32:
        print('3 подъезд')
    else:
        print('4 подъезд')
        # k=0 and w=room
        # для чётных чисел:  иначеесли room делится на цело на 16/на 24/на 32 и остаток равен 0, то 8 этаж, иначе  пока room < 32   w = w + 2  и  k=k+2 if w делится на цело на 16/на 24/на 32 , то   print('Этаж',' ',8-k)
        # если room <=8,то print ('Этаж',' ',room)
        # для нечётных чисел:  иначеесли room делится на цело на 15/на 23/на 31 и остаток равен 0, то 7 этаж, иначе  пока room < 32   w = w + 2  и  k=k+2 if w делится на цело на 15/на 23/на 31 , то   print('Этаж',' ',7-k)

if room
