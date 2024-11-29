import pylab as plt
import numpy as npy
t = npy.arange(0.0, 6.4, 0.1)
y = 5*npy.sin(t)
plt.plot(t, y, linewidth=2.0)
plt.xlabel('Zeit in Sekunden')
plt.ylabel('y(t)')
plt.title('Die Funktion y(t)=5*sin(t)')
plt.grid(True)
plt.show()


