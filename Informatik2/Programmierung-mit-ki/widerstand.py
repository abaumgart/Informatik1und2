"""Einfache Klasse zur Verdeutlichung des Umgangs mit elektrischen Widerständen.

Das Skript ist bewusst knapp, aber nachvollziehbar kommentiert, damit es für
Studierende gut verständlich bleibt.
"""


class Widerstand:
    """Repräsentiert einen elektrischen Widerstand mit ganzzahligem Wert."""

    def __init__(self, r: int) -> None:
        """Legt beim Erzeugen eines Objekts den Widerstandswert fest."""
        self.r = r

    def set_r(self, r: int) -> None:
        """Setzt den Widerstandswert auf einen neuen ganzzahligen Wert."""
        self.r = r

    def get_r(self) -> int:
        """Gibt den aktuell gespeicherten Widerstandswert zurück."""
        return self.r
