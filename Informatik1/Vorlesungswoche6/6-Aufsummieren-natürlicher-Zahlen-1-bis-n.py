n = int(input("Bitte eine ganze Zahl n eingeben: "))				#1
summe = 0										#2
for i in range(1,n+1):								#3
      summe = summe + i								#4
print("Die Summe der Zahlen von 1 bis %d ist %d" % (n, summe)) 		#5
