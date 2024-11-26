# Abstand zweier Punkte in der Ebene

from math import sqrt                                    #1

def dist(xa,ya,xb,yb):                                     #2
      """dist - Berechnet den Abstand	         #9
      zweier Punkte. Übergabeparameter
      sind xa,ya (erster Punkt) und xb,yb
      (zweiter Punkt)"""
      abstand = sqrt((xa-xb)**2+(ya-yb)**2)       #3
      return abstand                                         #4

# Punkt 1                                 			#5
x1 = 0.0; y1 = 0.0
# Punkt 2
x2 = 10.0; y2 = 10.0

# Punkt 3
x3 = 0.0; y3 = 10.0

# Abstand von Punkt 1 und Punkt 2
ap1p2 = dist(x1,y1,x2,y2)     #6
print("Der Abstand zwischen Punkt 1 und Punkt 2 ist ", ap1p2)

# Abstand von Punkt 2 und Punkt 3
ap2p3 = dist(x3,y3,x2,y2)     #7
print("Der Abstand zwischen Punkt 3 und Punkt 2 ist ", ap2p3)

# Abstand von Punkt 1 und Punkt 3
ap1p3= dist(x1,y1,x3,y3)      #8
print("Der Abstand zwischen Punkt 1 und Punkt 3 ist ", ap1p3)
