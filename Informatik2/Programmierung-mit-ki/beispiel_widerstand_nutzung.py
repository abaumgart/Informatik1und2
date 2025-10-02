"""Kleines Beispielprogramm zur Nutzung der Widerstandsklasse und einer Reihenschaltung.

Die Kommentare sind so formuliert, dass Studierende jeden Schritt gut
nachvollziehen können.
"""

from reihenschaltung import Reihenschaltung
from widerstand import Widerstand


def main() -> None:
    """Erzeugt Widerstandsobjekte und berechnet ihren Gesamtwiderstand in einer Reihe."""
    # Wir legen zwei einzelne Widerstände an, die jeweils einen festen Ohm-Wert haben.
    erster_widerstand = Widerstand(r=220)
    zweiter_widerstand = Widerstand(r=330)

    # Nun kombinieren wir beide Bauteile zu einer Reihenschaltung.
    reihe = Reihenschaltung(erster=erster_widerstand, zweiter=zweiter_widerstand)

    # Die get_r-Methode der Reihenschaltung addiert die Einzelwerte und liefert den Gesamtwiderstand.
    print("Gesamtwiderstand in Ohm:", reihe.get_r())


if __name__ == "__main__":
    main()
