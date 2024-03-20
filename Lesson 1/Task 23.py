def my_filter(a):
    # умножаем каждый элемент списка на 10
    a = [str(i*10) for i in a]
    result = ' '.join(a)

    return result

dat = input()
numbers = [int(num) for num in dat.split()]

result = my_filter(numbers)
print(result)


