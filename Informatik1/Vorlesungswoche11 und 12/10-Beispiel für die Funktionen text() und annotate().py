import pylab as plt
import numpy as npy
t = npy.arange(0.0, 6.4, 0.1)
y = 5*npy.sin(t)
plt.plot(t,y,"ro-",linewidth=3)
plt.title("Sinus-Funktion")
plt.text(1.5,5.2,"Maximum")
plt.text(4.5,-5.5,"Minimum")
plt.annotate("Nulldurchgang",xy=(3.2,0), 
             xytext=(5,5), arrowprops={"facecolor":"b"})
plt.show()

