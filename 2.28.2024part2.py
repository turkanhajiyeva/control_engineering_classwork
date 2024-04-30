import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn

t = np.arange(0, 15, 0.01)

G = cn.tf([1], [1, 1, 0])

Kd = 0

K = 10

C = cn.tf([Kd, K], [1])

clsys = C * G / (1 + C * G)

# for K in np.arange(1, 10, 2):
for Kd in np.arange(0.1, 3, 0.5): # when we increase Kd values oscillations decrease and settling time decreases as well
    C = cn.tf([Kd, K], [1]) # derivate term makes the system more stable
    clsys = C * G / (1 + C * G)
    y, T = cn.step(clsys, t)
    plt.plot(t, y, label = 'Kd=' + str(Kd))

plt.figure()
plt.plot(t, y, label='Kd=' + str(Kd))
plt.legend()
plt.show()

