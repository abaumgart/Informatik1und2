a = int(input("Bitte Kathetenlaenge eingeben: "))
b = int(input("Bitte Kathetenlaenge eingeben: "))
c = int(input("Bitte Hypothenuse eingeben: "))
print("Ihre Eingaben: ",a,b,c)
if a**2+b**2==c**2:
      print("Das Dreieck ist rechtwinklig")
else:
      print("Das Dreieck ist NICHT rechtwinklig")

# Hinweis: Als Eingabe kommen nur ganze Zahlen (int)
# infrage. Bei Gleitkommazahlen kann ein Test auf
# Gleichheit scheitern!
