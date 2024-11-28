from turtle import *
from math import pi,cos,sin
minwert = -20
maxwert = 220
setworldcoordinates(minwert,minwert,maxwert,maxwert)
speed(0)

def linie(x1,y1,x2,y2,farbe="black",dicke=3):
    penup()
    pensize(dicke)
    pencolor(farbe)
    goto(x1,y1)
    pendown()
    goto(x2,y2)
    hideturtle()

def kreis(x,y,radius,farbe="black",dicke=3,n=8):	        #1
    winkel = 2*pi/n						#2
    xa = x + radius						#3
    ya = y							#4
    for i in range(n):						#5
        phi2 = winkel*(i+1)					#6
        xe = x + radius*cos(phi2)				#7
        ye = y + radius*sin(phi2)				#8
        linie(xa,ya,xe,ye,farbe,dicke)			        #9
        xa, ya = xe, ye						#10

# Koordinatenachsen + Ursprungspunkt
linie(0,0,50,0)
linie(0,0,0,50)
# Kreise zeichnen
kreis(50,50,15,farbe="red")
kreis(100,100,20,n=12,farbe="green")
kreis(150,150,18,n=16,farbe="blue")
kreis(200,200,15,n=20,farbe="brown")

print("Bitte zum Beenden in die Grafik klicken!")
exitonclick()


    

