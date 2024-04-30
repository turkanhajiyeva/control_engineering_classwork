import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn


t = np.arange(0, 35, 0.1)

G = cn.tf([1], [1, 0, 0])

Comp = cn.tf([1, 0], [1, 2])
LagComp = cn.tf([1, 0.1], [1, 0.01])
cn.rlocus(G * Comp)
plt.figure()

K = 2

clsys = K * G * Comp / (1 + K * G * Comp)
cn.pzmap(clsys)
plt.figure()
y, t = cn.step(clsys, t)
plt.plot(t,y)
plt.figure()

y, t, x = cn.lsim(clsys, np.sin(t), t)
plt.plot(t, y)
plt.plot(t, np.sin(t))


plt.show()
