import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

func = lambda f, t: f[1] + t

dt = 1e-3
t = np.arange(0, 1 + dt, dt)

res = odeint(func, y0=[0, 1], t=t)

plt.figure(figsize=(5, 4))
plt.plot(t, res[:, 0])
plt.plot(t[::50], np.exp(t[::50]), 'o')

plt.show()
f_at_t_1 = res[-1, 0]
rounded_f_at_t_1 = round(f_at_t_1, 2)

print(f"The value of f(t=1) is approximately {rounded_f_at_t_1}")