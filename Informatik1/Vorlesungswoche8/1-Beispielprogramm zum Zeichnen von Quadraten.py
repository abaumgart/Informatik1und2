from turtle import *
def Quadrat(x,y,Laenge,Farbe="black",Dicke=3):		#1
    pensize(Dicke)
    pencolor(Farbe)
    penup()
    goto(x,y)
    pendown()
    for i in range(4):
        forward(Laenge)
        left(90)

# Aufrufe der Funktion
Quadrat(0,0,100)							#2
Quadrat(100,-100,100)						#3
Quadrat(200,0,100,Farbe="red")					#4
				
exitonclick()
