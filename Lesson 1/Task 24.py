def trapez(func, a, b, N):
    h = (b - a) / N


    x_values = [a + i * h for i in range(N+1)]
    y_values = [func(x) for x in x_values]

    integr = sum(y_values) - (y_values[0] + y_values[N]) / 2
    integr *= h
    integr = round(integr, 8)

    return integr

def f(x):
    return x**2

a = int(input())
b = int(input())
N = int(input())

result = trapez(f, a, b, N)
print(result)
