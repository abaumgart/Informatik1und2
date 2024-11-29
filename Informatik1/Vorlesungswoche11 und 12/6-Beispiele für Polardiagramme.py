import pylab as plt
import numpy as npy
theta = npy.arange(361)
theta2 = npy.radians(theta)
r = 2*theta2
plt.polar(theta2,r)
plt.title('Archimedische Spirale')
plt.show()


