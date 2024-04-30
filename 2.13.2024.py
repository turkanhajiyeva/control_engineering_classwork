import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn

t = np.arange(0, 15, 0.01)

G = cn.tf([1], [1, 2, -3])


H = cn.tf([1], [1, 5])

K = 20

clsys = K * G / (1 + K * G * H)

y, T = cn.step(clsys, t)

plt.plot(t, y)

# cn.pzmap(clsys)


H = cn.tf([1], [1, 5])

K = 30

clsys = K * G / (1 + K * G * H)

y, T = cn.step(clsys, t)

plt.plot(t, y)


H = cn.tf([1], [1, 5])

K = 40

clsys = K * G / (1 + K * G * H)

y, T = cn.step(clsys, t)

plt.plot(t, y)


H = cn.tf([1], [1, 5])

K = 50

clsys = K * G / (1 + K * G * H)

y, T = cn.step(clsys, t)

plt.plot(t, y)


H = cn.tf([1], [1, 5])

K = 60

clsys = K * G / (1 + K * G * H)

y, T = cn.step(clsys, t)

plt.plot(t, y)

plt.plot(t, np.ones(t.size))

plt.show()
