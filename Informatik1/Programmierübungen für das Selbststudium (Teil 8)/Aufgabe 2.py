

import pylab as plt
import numpy as npy

t = npy.arange(0,63,0.01)
sinuswerte = npy.sin(t)				                #1
plt.hist(sinuswerte,bins=20,color="yellow",linewidth=2)		#2
plt.title('Histogramm einer Sinusfunktion')		        #3
plt.annotate("Maximalwerte",xy=(0.95,905),
             xytext=(0,920), arrowprops={"facecolor":"b"})      #4

plt.show()



