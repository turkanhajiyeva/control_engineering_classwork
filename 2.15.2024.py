import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn

t = np.arange(0, 20, 0.01)

wn = 1
z = 0.6

# for z in np.arange(0, 1, 0.2):
sys = cn.tf([wn ** 2], [1, 2 * z * wn, wn ** 2])
y, T = cn.step(sys, t)
plt.plot(t, y)

plt.show()
