import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn

t = np.arange(0, 10, 0.01)

# G = cn.tf([1,2], [1,1,0])

# x = cn.zpk2tf([-2], [0,-1],1) # showing arrays s+2 / s s+1

# x = cn.zpk2tf([-5], [-1,-3],1)
x = cn.zpk2tf([ ], [2, -2,-5],1)


G = cn.tf(x[0], x[1])
print(G)
K = 70

# G = cn.tf([1,1], [1,2,0])
cn.rlocus(G)
# K = 5.5
clsys = K * G / (1 + K * G)
plt.figure()
cn.pzmap(clsys)

plt.show()
