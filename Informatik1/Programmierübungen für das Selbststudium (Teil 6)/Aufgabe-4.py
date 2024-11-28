from geometrie2 import *
from random import randrange

minwert = 0; maxwert = 100
# Mit tracer(False) wird nur das Endergebnis
# des Zeichenprozesses gezeigt! Das ist schneller!
tracer(False)
setworldcoordinates(minwert,minwert,maxwert,maxwert)

def kreuz(x,y,laenge=1,farbe="black",dicke=3):
    linie(x,y,x+laenge,y,farbe,dicke)
    linie(x,y,x-laenge,y,farbe,dicke)    
    linie(x,y,x,y+laenge,farbe,dicke)    
    linie(x,y,x,y-laenge,farbe,dicke)

for i in range(100):
    x = randrange(minwert,maxwert)
    y = randrange(minwert,maxwert)
    kreuz(x,y)

print("Bitte zum Beenden in die Grafik klicken!")

exitonclick()
