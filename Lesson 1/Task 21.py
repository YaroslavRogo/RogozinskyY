x = input().split()
x = [int(pos) for pos in x]
max_v = 0
for i in range(1, len(x)):
    v = abs(x[i] - x[i - 1]) / 0.01
    if v > max_v:
        max_v = v

print(max_v)