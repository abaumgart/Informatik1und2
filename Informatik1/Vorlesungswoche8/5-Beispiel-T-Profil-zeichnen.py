from turtle import *
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

# Koordinatenachsen + Ursprung
linie(0,0,50,0)
linie(0,0,0,50)
# T-Profil zeichnen
linie(50,150,150,150,dicke=4)
linie(50,150,50,120,dicke=4)
linie(150,150,150,120,dicke=4)
linie(50,120,80,120,dicke=4)
linie(150,120,120,120,dicke=4)
linie(80,120,80,30,dicke=4)
linie(120,120,120,30,dicke=4)
linie(80,30,120,30,dicke=4)

exitonclick()
