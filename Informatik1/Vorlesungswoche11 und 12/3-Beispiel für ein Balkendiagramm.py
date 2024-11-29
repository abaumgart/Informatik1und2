import pylab as plt
import numpy as npy
quartal = [1,2,3,4]
umsatz = [120000,154000,133000,198000]
plt.bar(quartal,umsatz,width=0.3,align="center")
plt.xlabel('Quartal des Jahres 2011')
plt.ylabel('Umsatz')
plt.title('Umsatzentwicklung in 2011')
plt.grid(True)
plt.show()


