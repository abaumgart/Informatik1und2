inhalt = [ 23.5, 12, [19, "Hallo"], 12, 45]
print(inhalt)							#1
inhalt.append(100)						#2
print(inhalt)
inhalt[2].append(200)					#3
print(inhalt)
anzahl = inhalt.count(12)					#4
print(anzahl)
inhalt.remove(23.5)						#5
print(inhalt)
ind = inhalt.index(45)					#6
print(ind)
inhalt.insert(3,77)						#7
print(inhalt)




