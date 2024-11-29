import pylab as plt
import numpy as npy
quartal = [1,2,3,4]
umsatz = [120000,154000,133000,198000]
plt.barh(quartal,umsatz,height=0.3,align="center",\
         color="yellow", edgecolor="black", linewidth=3)
plt.ylabel('Quartal des Jahres 2011')
plt.xlabel('Umsatz')
plt.title('Umsatzentwicklung in 2011')
plt.grid(True)
plt.show()


