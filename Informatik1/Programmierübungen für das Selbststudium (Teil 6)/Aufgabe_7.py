from math import sqrt

def quadratische_gleichung(p,q):
    Radikand = (p/2.)**2-q
    if Radikand<0.:
        print("Keine reelle Loesung!")
    else:
        x1 = -p/2.+sqrt(Radikand)
        x2 = -p/2.-sqrt(Radikand)
        print("Loesungen:")
        print("x1 = ",x1)
        print("x2 = ",x2)

# Hauptprogramm
p = float(input("Bitte p eingeben: "))
q = float(input("Bitte q eingeben: "))
quadratische_gleichung(p,q)






        



    

