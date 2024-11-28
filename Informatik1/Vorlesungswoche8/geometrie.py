# Moduldatei zu Aufgabe 6 Kapitel 3.11
# Variante für Python 3.2

from turtle import *
from math import pi,cos,sin
speed(0)

def linie(x1,y1,x2,y2,farbe="black",dicke=3):
    penup()
    pensize(dicke)
    pencolor(farbe)
    goto(x1,y1)
    pendown()
    goto(x2,y2)
    hideturtle()
def kreis(x,y,radius,farbe="black",dicke=3,n=8):	        
    winkel = 2*pi/n						
    xa = x + radius						
    ya = y
    for i in range(n):						
        phi2 = winkel*(i+1)					
        xe = x + radius*cos(phi2)				
        ye = y + radius*sin(phi2)				
        linie(xa,ya,xe,ye,farbe,dicke)			        
        xa, ya = xe, ye						
def kreuz(x,y,laenge=1,farbe="black",dicke=3):
    linie(x,y,x+laenge,y,farbe,dicke)
    linie(x,y,x-laenge,y,farbe,dicke)    
    linie(x,y,x,y+laenge,farbe,dicke)    
    linie(x,y,x,y-laenge,farbe,dicke)

def Quadrat(x,y,Laenge,Farbe="black",Dicke=3):		#1
    pensize(Dicke)
    pencolor(Farbe)
    penup()
    goto(x,y)
    pendown()
    for i in range(4):
        forward(Laenge)
        left(90)
