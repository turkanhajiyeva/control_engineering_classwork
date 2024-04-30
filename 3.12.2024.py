import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn

t = np.arange(0, 10, 0.01)

G = cn.tf([1], [1, 2, 0])

K = 5

# large oscilations less error

for K in np.arange(1, 10, 1):
    clsys = K * G / (1 + K * G)
    y, T = cn.step(clsys, t)
    plt.plot(t, y)

plt.figure()
for K in np.arange(1, 10, 1):
    clsys = K * G / (1 + K * G)
    y, T, x = cn.lsim(clsys, t, t)
    plt.plot(t, y)

plt.plot(t, t)
plt.show()
