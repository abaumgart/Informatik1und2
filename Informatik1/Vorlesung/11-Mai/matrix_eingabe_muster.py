# Matrix: zuerst Zeilen- und Spaltenzahl, dann jeden Wert einlesen und in einer Liste speichern.

anzahl_zeilen = int(input("Anzahl Zeilen: "))
anzahl_spalten = int(input("Anzahl Spalten: "))

matrix = []

for zeile_index in range(anzahl_zeilen):
    zeile = []
    for spalte_index in range(anzahl_spalten):
        text = input(
            "Wert [Zeile " + str(zeile_index + 1) + ", Spalte " + str(spalte_index + 1) + "]: "
        )
        wert = float(text.replace(",", "."))
        zeile.append(wert)
    matrix.append(zeile)

print(matrix)
