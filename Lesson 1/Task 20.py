ch = float(input())
lns = 0
n =0
ln = ((-1)**n * ch**(n+1))/(n+1)
while abs(ln) > 1e-06:
      lns = lns + ln
      n = n + 1
      ln = ((-1) ** n * ch ** (n + 1)) / (n + 1)

print(round(lns, 8))
