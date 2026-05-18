a=[1,3,5,7,9]
b=[2,'Hallo', 12.5]
c=[[2,4],["a","b"]]
print(b[1])
print(c[1][1])
#farbe=input("Geben Sie eine Farbe ein:")
farben=["rot","grün","blau"]
print(len(farben))
anzahl=len(farben)
# if farbe not in farben:
#    print("Farbe ist nicht vorhanden")

for i in range(0,anzahl,1):
    print(i, farben[i])

for i in farben:
    print(i)
    
