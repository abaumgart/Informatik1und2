import pylab as plt
import numpy as npy
t = npy.arange(0.0, 6.4, 0.1)
y = 5*npy.sin(t)
z = 3*npy.cos(t)
gesamt = plt.figure()
diag1 = gesamt.add_subplot(1,2,1)
diag1.plot(t,y,color="red",linewidth=3)
diag1.set_title("Sinus-Funktion")
diag2 = gesamt.add_subplot(1,2,2)
diag2.plot(t,z,color="blue",linewidth=2)
diag2.set_title("Kosinus-Funktion")
gesamt.show()


