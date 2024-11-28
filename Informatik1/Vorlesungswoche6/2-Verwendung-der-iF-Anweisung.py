# Berechnung der Quadratwurzel
from math import sqrt
zahl = float(input("Bitte eine Zahl eingeben: "))
if zahl >= 0.0:
      wurzel = sqrt(zahl)
      print("Die Wurzel aus %f ist %f " % (zahl, wurzel))
if zahl < 0.0:
      print("Aus einer negativen Zahl kann keine")
      print("Quadratwurzel berechnet werden.")
      print("Geben Sie eine positive Zahl ein!")
