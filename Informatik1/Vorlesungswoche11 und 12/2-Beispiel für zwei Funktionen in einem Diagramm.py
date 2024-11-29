import pylab as plt
import numpy as npy
t = npy.arange(0.0, 6.4, 0.1)
y = 5*npy.sin(t)
z = 3*npy.cos(t)
plt.plot(t, y, "r+", t, z, "bo", linewidth=2.0)
plt.xlabel('Zeit in Sekunden')
plt.ylabel('y(t), z(t)')
plt.title('Die Funktionen y(t)=5*sin(t) und z(t)=3*cos(t)')
plt.grid(True)
plt.show()


