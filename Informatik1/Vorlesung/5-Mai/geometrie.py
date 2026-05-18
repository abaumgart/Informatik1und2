# geometrie.py

PI = 3.14159


def ist_positiv(wert):
    """Prüft, ob ein Wert größer als 0 ist."""
    return wert > 0


def flaeche_quadrat(seitenlaenge):
    return seitenlaenge * seitenlaenge


def umfang_quadrat(seitenlaenge):
    return 4 * seitenlaenge


def flaeche_rechteck(laenge, breite):
    return laenge * breite


def umfang_rechteck(laenge, breite):
    return 2 * (laenge + breite)


def flaeche_kreis(radius):
    return PI * radius * radius


def umfang_kreis(radius):
    return 2 * PI * radius