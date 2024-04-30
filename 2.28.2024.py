import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn

t = np.arange(0, 15, 0.01)

G = cn.tf([1], [1, 1, 0])
# K = 0.7
# K = 1.5
# oscillations get larger, overshoot is larger than 0.1
# K = 0.3
# response is slow
K = 2
# when we make it 2 for ramp input, the steady state error is smaller.

# in step response, we will get larger oscillations which means it is
# going to be faster but less stable.

clsys = K * G / (1 + K * G)

# y, T = cn.step(clsys, t)
y, T, x = cn.lsim(clsys, t, t)

plt.plot(t, y)
plt.plot(t, t)
plt.show()

# print(G)

# if we do the same system for ramp, steady state error is going to larger.
# when you increase K, it is going to have less steady state error