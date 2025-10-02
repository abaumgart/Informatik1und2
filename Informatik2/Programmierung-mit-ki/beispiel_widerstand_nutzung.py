"""Kleines Beispielprogramm zur Nutzung der Widerstandsklasse.

Die Kommentare sind so formuliert, dass Studierende jeden Schritt gut
nachvollziehen können.
"""

from widerstand import Widerstand


def main() -> None:
    """Erzeugt ein Widerstandsobjekt und demonstriert die Zugriffsmethoden."""
    # Wir legen einen Widerstand mit 220 Ohm an.
    widerstand = Widerstand(r=220)
    print("Anfangswert in Ohm:", widerstand.get_r())

    # Nun ändern wir den Wert auf 330 Ohm, um den Setter zu zeigen.
    widerstand.set_r(r=330)
    print("Neuer Wert in Ohm:", widerstand.get_r())


if __name__ == "__main__":
    main()
