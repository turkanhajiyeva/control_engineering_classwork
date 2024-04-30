import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn

t = np.linspace(0, 15, 1000)

G = cn.tf([1], [1, 2, 0])

K = cn.tf([Kd, K, Ki], [1,0])

K = 10
Ki = 5
Kd = 3
clsys = K * G / (1 + K * G)

yr, T = cn.step(clsys, t)

clsys = G / (1 + K * G)

yd, T = cn.step(clsys, t[500:1000])

yr[500:1000] = yr[500:1000] + yd # overall y

plt.plot(t, yr)
plt.show()