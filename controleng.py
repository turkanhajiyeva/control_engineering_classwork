import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn

t = np.arange(0, 300, 0.1)
# t = np.linspace(0, 300, 100)

G = cn.tf([1, 2], [1, 3, 4])
H = cn.tf([1],[1,5])

clsys = G/(1 + G * H)

# cn.pzmap(clsys)
# print(H)

u = np.sin(t) + 2 * np.cos( t / 5)

y, T, x = cn.lsim(clsys, u, t)

# y, T = cn.step(clsys, t)
# plt.plot(t, y)
# plt.figure()
plt.plot(t, np.ones(t.size))
plt.plot(t, y)
plt.plot(t, u)
plt.show()