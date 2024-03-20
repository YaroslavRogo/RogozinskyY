def write(filename, data):
    with open(filename, "w") as file:
        for D in data:
            time, value = D
            line = f"{time}\t{value}\n"
            file.write(line)

filename = "1.txt"
data = [(1, 20), (2, 30), (3, 40), (4, 35), (5, 22), (6, 10)]

write(filename, data)