eineListe=[2,5, 10,7]
summe=0
anzahlElemente =len(eineListe)

print(eineListe)
eineListe.sort()
print(eineListe)
eineListe.reverse()
print(eineListe)
#Wert anhängen
eineListe.append(45)
print(eineListe)
#Wert löschen
eineListe.remove(5)
print(eineListe)
#Wert an bestimmer Position einfügen
eineListe.insert(2,111)
print(eineListe)
#Wert an bestimmer Position löschen
del eineListe[2]
print(eineListe)
#Maximalwert bestimmen
print(max(eineListe))
#Minimalwert bestimmen
print(min(eineListe))
#Summe der werte einer Liste bestimmen
print(sum(eineListe))
#for i in range(0,anzahlElemente,1):
 #   summe=eineListe[i]+summe
#print (summe/anzahlElemente)
 
 # 3x3 Matrix
 
meineMatrix=[
                 [1,2,3],#erste Zeile
                 [4,5,6],#zweite Zeile
                 [7,8,9],#dritte Zeile
                ]
 #Zugriff auf das Element in der zweiten Zeile,
 #dritten Spalte
element=meineMatrix[1][2]
print(element)