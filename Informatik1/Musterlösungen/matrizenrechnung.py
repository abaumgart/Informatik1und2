import numpy as np
print("Dieses Programm erfasst eine Matrix.")
werte_pro_zeile = int(input("Wie viele Werte soll jede Zeile enthalten? "))
anzahl_zeilen = int(input("Wie viele Zeilen soll die Matrix haben? "))
matrix1liste = []
matrix2liste = []
gesamt_anzahl = werte_pro_zeile * anzahl_zeilen

print("\nBitte nun für Matrix 1", gesamt_anzahl, "Werte eingeben.")
for i in range(gesamt_anzahl):
    wert = float(input(f"Wert {i+1} eingeben: "))
    matrix1liste.append(wert)
    
print("\nBitte nun für Matrix 2", gesamt_anzahl, "Werte eingeben.")
for i in range(gesamt_anzahl):
    wert = float(input(f"Wert {i+1} eingeben: "))
    matrix2liste.append(wert)
    
print(matrix1liste)
print(matrix2liste)
#Umwandlung in Array für NumPy
arrayMatrix1zweid= np.array(matrix1liste).reshape(anzahl_zeilen,werte_pro_zeile)
arrayMatrix2zweid= np.array(matrix2liste).reshape(anzahl_zeilen,werte_pro_zeile)
print(arrayMatrix1zweid)
print(arrayMatrix1zweid)

#Matrizenmultiplikation
matrix = arrayMatrix1zweid@arrayMatrix1zweid
print(matrix)

