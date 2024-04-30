import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn

# t= np.arange(0, 20, 0.01)

t = np.linspace(0, 20, 2000)

K = 4

Ki = 1
# without integral control, disturbance olanda 0a getmiyecek. steady olmayacaq

Kd = 1

# Kd is derivative term decrease the overshoot and oscillations

C = cn.tf([Kd,K,Ki], [1,0])

G = cn.tf([1],[1, 1, 0])

# [1, 1]
# s + 1
# [1, 1, 1]
# s^2 + s + 1

sysR = C * G / (1+ C*G)

yr, T = cn.step(sysR, t)

# T = t

sysD = G / (1 + G * C)

yd, T = cn.step(sysD, t[0:1000])

# t[0:1000] half size

y = yr

# y[1000:-1] excludes last element

y[1000:2000] = y[1000:2000] + yd * 0.3

plt.plot(t, y)

plt.plot(t, np.ones(t.size))
plt.show()





