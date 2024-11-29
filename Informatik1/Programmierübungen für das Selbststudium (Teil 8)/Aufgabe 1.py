

import pylab as plt
import numpy as npy

t = npy.arange(0.0, 2.1, 0.1)
y1 = npy.exp(-t)
y2 = npy.exp(-2*t)
y3 = npy.exp(-4*t)
plt.plot(t, y1, "r+-", linewidth=2.0, label="k=1")
plt.plot(t, y2, "bo-", linewidth=2.0, label="k=2")
plt.plot(t, y3, "g^-", linewidth=2.0, label="k=3")
plt.xlabel('Zeit in Sekunden')
plt.ylabel('y(t)')
plt.title('Die Funktion y(t)=exp(-k*t) fuer k=1,2,4')
plt.legend(("k=1","k=2","k=4"))
plt.show()


