from geometrie2 import *

rein = open("Ergebnisse2.txt","r")
inhalt = rein.readlines()
rein.close()
X=[]; Y=[]; Z=[]; W=[]
for i in 0,1,2:
    del inhalt[0]
for i in inhalt:
    j = i.replace(",",".") 
    x,y,z,w = j.split()
    X.append(float(x))
    Y.append(float(y))
    Z.append(float(z))
    W.append(float(w))

wmax = max(W);

setworldcoordinates(-10,-10,210,210)
s = 0
tracer(False) # Zeigt nur das Endergebnis
speed(s)
    
def kreuz(x,y,laenge=1,farbe="black",dicke=3):
    linie(x,y,x+laenge,y,farbe,dicke)
    linie(x,y,x-laenge,y,farbe,dicke)    
    linie(x,y,x,y+laenge,farbe,dicke)    
    linie(x,y,x,y-laenge,farbe,dicke)
yiter = iter(Y); ziter = iter(Z); witer = iter(W)
for i in X:
    y = next(yiter)
    z = next(ziter)
    w = next(witer)
    rel = w/wmax
    if rel<0.25:
        farbe = "blue"
    elif 0.25<=rel<0.5:
        farbe = "green"
    elif 0.5<=rel<0.75:
        farbe = "yellow"
    else:
        farbe = "red"
    speed(s)
    penup()
    goto(y,z)
    pendown()
    kreuz(y,z,farbe=farbe,laenge=2)

print("Bitte zum Beenden in die Grafik klicken!")

exitonclick()
