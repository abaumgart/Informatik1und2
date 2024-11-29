import pylab as plt
import numpy as npy
zahlen = npy.random.randn(10000)
plt.hist(zahlen,bins=20,color="yellow",linewidth=2)
plt.title('Histogramm normalverteilter Zufallszahlen\n')
plt.show()


