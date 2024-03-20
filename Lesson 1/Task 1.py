def f_ent(room):
    numb = 8   # количество этажей

    pod = ((room - 1) // numb ) + 1

    return pod


def f_fl(room):
    numb = 8
    floor = ((room - 1) % numb*8) //  numb + 1  # определение этажа
    return  floor


room = int(input("Введите номер квартиры: "))
floor = f_fl(room)
pod = f_ent(room)
print("Этаж:", floor)
print("Подъезд:", pod)