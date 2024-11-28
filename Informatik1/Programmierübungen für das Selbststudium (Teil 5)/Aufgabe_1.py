werte = [12, 22, 'Wuppertal', 34.5, "Solingen", 102.45, 103, 12.3, 45]

Ganzezahlen = []
Gleitpunktzahlen = []
Zeichenketten = []

for x in werte:
    if type(x)==int:
        Ganzezahlen.append(x)
    elif type(x)==float:
        Gleitpunktzahlen.append(x)
    elif type(x)==str:
        Zeichenketten.append(x)
print()
print(Ganzezahlen)
print(Gleitpunktzahlen)
print(Zeichenketten)


