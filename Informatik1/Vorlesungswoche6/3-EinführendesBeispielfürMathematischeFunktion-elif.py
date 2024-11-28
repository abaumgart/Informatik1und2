x = float(input("Bitte x eingeben: "))
if x <= 0.0:				#1
      y = 0.0
elif 0.0 < x < 1.0:			#2
      y = x
else:					#3
      y = 1.0
print(y)   
