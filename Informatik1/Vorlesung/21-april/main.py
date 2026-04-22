# main.py

import geometrie


def zahl_einlesen(frage_text):
    """Liest eine Kommazahl ein und gibt sie zurück."""
    eingabe_text = input(frage_text)
    zahl = float(eingabe_text)
    return zahl


def dreiecksmuster_ausgeben(hoehe):
    """Gibt ein einfaches Sternchen-Dreieck aus."""
    for zeile in range(1, hoehe + 1):
        print("*" * zeile)


def menue_anzeigen():
    print("\n--- Geometrie-Werkstatt ---")
    print("1 - Quadrat berechnen")
    print("2 - Rechteck berechnen")
    print("3 - Kreis berechnen")
    print("4 - Dreiecksmuster anzeigen")
    print("0 - Beenden")


programm_laeuft = True

while programm_laeuft:
    menue_anzeigen()
    auswahl_text = input("Bitte Auswahl eingeben: ")

    if auswahl_text == "1":
        seitenlaenge = zahl_einlesen("Seitenlänge des Quadrats: ")

        if geometrie.ist_positiv(seitenlaenge):
            flaeche = geometrie.flaeche_quadrat(seitenlaenge)
            umfang = geometrie.umfang_quadrat(seitenlaenge)

            print(f"Fläche: {flaeche:.2f}")
            print(f"Umfang: {umfang:.2f}")
        else:
            print("Fehler: Die Seitenlänge muss größer als 0 sein.")

    elif auswahl_text == "2":
        laenge = zahl_einlesen("Länge des Rechtecks: ")
        breite = zahl_einlesen("Breite des Rechtecks: ")

        if geometrie.ist_positiv(laenge) and geometrie.ist_positiv(breite):
            flaeche = geometrie.flaeche_rechteck(laenge, breite)
            umfang = geometrie.umfang_rechteck(laenge, breite)

            print(f"Fläche: {flaeche:.2f}")
            print(f"Umfang: {umfang:.2f}")
        else:
            print("Fehler: Länge und Breite müssen größer als 0 sein.")

    elif auswahl_text == "3":
        radius = zahl_einlesen("Radius des Kreises: ")

        if geometrie.ist_positiv(radius):
            flaeche = geometrie.flaeche_kreis(radius)
            umfang = geometrie.umfang_kreis(radius)

            print(f"Fläche: {flaeche:.2f}")
            print(f"Umfang: {umfang:.2f}")
        else:
            print("Fehler: Der Radius muss größer als 0 sein.")

    elif auswahl_text == "4":
        hoehe_text = input("Höhe des Dreiecks (ganze Zahl): ")
        hoehe = int(hoehe_text)

        if hoehe > 0:
            dreiecksmuster_ausgeben(hoehe)
        else:
            print("Fehler: Die Höhe muss größer als 0 sein.")

    elif auswahl_text == "0":
        programm_laeuft = False
        print("Programm beendet. Tschüss!")

    else:
        print("Ungültige Auswahl. Bitte 0, 1, 2, 3 oder 4 eingeben.")