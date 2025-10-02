"""Repräsentiert eine einfache Reihenschaltung aus zwei Widerständen.

Die Kommentare erläutern jeden Schritt so, dass Studierende die Has-A-Beziehung
zwischen Reihenschaltung und den enthaltenen Widerständen gut nachvollziehen
können.
"""

from widerstand import Widerstand


class Reihenschaltung:
    """Modelliert zwei in Reihe geschaltete Widerstände."""

    def __init__(self, erster: Widerstand, zweiter: Widerstand) -> None:
        """Speichert die beiden Widerstandsobjekte der Reihenschaltung."""
        # Die Reihenschaltung besitzt ("has-a") zwei Widerstandsobjekte.
        self.erster = erster
        self.zweiter = zweiter

    def get_r(self) -> int:
        """Gibt den Gesamtwiderstand der beiden in Reihe liegenden Widerstände zurück."""
        # Der Gesamtwiderstand einer Reihenschaltung ergibt sich durch Addition beider Werte.
        return self.erster.get_r() + self.zweiter.get_r()
