import pylab as plt
import numpy as npy
stimmen = [14658515,9990488,6316080,4643272,5155933,2606902]
parteien = ["CDU/CSU", "SPD", "FDP", "GRUENE", "DIE LINKE", "Sonstige"]
plt.pie(stimmen,labels=parteien)
plt.title('Bundestagswahl 2009')
plt.show()


