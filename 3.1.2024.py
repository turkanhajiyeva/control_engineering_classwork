import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn

t = np.arange(0, 15, 0.01)

G = cn.tf([1], [1, 2])

# K = 1
# K = 3  when we increase K value, steady state error decreases

K = 3
Ki = 2
# Ki = 0 without integral control the steady state error is going to be large

for K in np.arange(1, 7):
    C = cn.tf([K, Ki], [1, 0])
    # clsys = K * G / (1 + K * G)
    clsys = C * G / (1 + C * G)
    y, T = cn.step(clsys, t)
    plt.plot(t, y)
plt.plot(t, np.ones(t.size))

plt.show()