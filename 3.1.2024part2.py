import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn

t = np.arange(0, 15, 0.01)

G = cn.tf([1], [1, 2, 0])

K = 10
# Ki = 3
# C = cn.tf([K, Ki], [1, 0])
# for Kd in np.arange(0, 3.5, 3):
# C = cn.tf([Kd, K], [1])
# clsys = C * G / (1 + C * G)
clsys = K * G / (1 + K * G)
# y, T = cn.step(clsys, t)
y, T, x = cn.lsim(clsys, t, t)
plt.plot(t, y)
plt.plot(t, t)
# plt.plot(t, np.ones(t.size))

plt.show()