x = float(input("Bitte x-Koordinate des Punktes eingeben: "))
y = float(input("Bitte y-Koordinate des Punktes eingeben: "))

if x>=0:
      if y>=0:
            quadrant = 1
      else:
            quadrant = 4
else:
      if y>=0:
            quadrant = 2
      else:
            quadrant = 3
            
print("Der Punkte liegt im ",quadrant,".ten Quadranten")
