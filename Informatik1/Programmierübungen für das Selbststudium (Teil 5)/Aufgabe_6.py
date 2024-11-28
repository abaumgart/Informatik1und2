
Woerterbuch = {}
wortDE = input("Bitte ein deutsches Wort eingeben: ")
while wortDE!="":
    wortEN = input("Bitte ein englisches Wort eingeben: ")
    # Ist ein Schlüssel schon vorhanden?
    if wortDE in Woerterbuch.keys():
        # Schlüssel ist schon vorhanden
        print("Warnung! Ein Eintrag ist schon vorhanden!")
        print("Schluessel: ",wortDE," Wert: ", Woerterbuch[wortDE])
        antwort = input("Sollen diese Werte ueberschrieben werden? (j/n)")
        if antwort.upper()=="J":
            Woerterbuch[wortDE] = wortEN
    else:
        # Schlüssel ist noch nicht vorhanden
        Woerterbuch[wortDE] = wortEN
    wortDE = input("Bitte ein deutsches Wort eingeben: ")
print(Woerterbuch)


    

