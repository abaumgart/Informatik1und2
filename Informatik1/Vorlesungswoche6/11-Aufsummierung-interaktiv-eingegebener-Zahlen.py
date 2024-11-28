print("Summation von Zahlen - Bitte geben Sie Zahlen ein!")			#1
print("(Abbruch durch Eingabe einer Null)")					#2
print()											#3
zahl = 1										#4
anzahl = 0										#5
summe = 0										#6
while zahl!=0:									#7
      zahl = int(input("Bitte die Zahl oder Null eingeben: "))			#8
      summe += zahl									#9
      anzahl +=1									#10
anzahl -=1										#11
print("Die Summe der eingegebenen Zahlen ist %d" % (summe))		#12
print("Sie haben %d Zahlen eingegeben" % (anzahl))				#13
