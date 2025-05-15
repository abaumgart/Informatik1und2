def wertevergleich(wert):
    if wert < 0:
        print("Der eingegebene Wert ist kleiner als null.")
    else:
        print("Der eingegebene Wert ist null oder größer.")

def main():
    for _ in range(3):
            wert = float(input("Bitte geben Sie eine Zahl ein: "))
            wertevergleich(wert)
        
main()