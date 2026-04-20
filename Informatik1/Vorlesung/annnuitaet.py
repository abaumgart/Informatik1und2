from invfin import *


KW = float(input("Kapitalwert: "))

p = int(input("Prozent: "))

j= int(input("Jahre: "))

p=p/100

Ann = annuitaet(KW,p,j)

print("Ann = ",Ann)