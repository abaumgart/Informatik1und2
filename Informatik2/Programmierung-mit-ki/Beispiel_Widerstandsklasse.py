"""Ein kleines Beispiel für eine Widerstandsklasse.

Das Skript ist bewusst ausführlich kommentiert, damit Studierende beim Lesen
nachvollziehen können, wie eine Klasse in Python aufgebaut ist und wie man mit
Instanzen dieser Klasse arbeitet.
"""

from __future__ import annotations


class Widerstand:
    """Repräsentiert einen elektrischen Widerstand mit typischen Kenngrößen."""

    def __init__(self, ohm: float, toleranz: float = 0.05, leistung: float = 0.25) -> None:
        """Legt die Basisdaten für den Widerstand fest.

        Parameter
        ---------
        ohm: float
            Der Nennwert des Widerstands in Ohm (Ω). Er darf nicht Null sein, da man
            sonst keine Strom- oder Spannungswerte berechnen kann.
        toleranz: float, optional
            Toleranz des Bauteils als relativer Anteil (z.B. 0.05 für ±5 %).
        leistung: float, optional
            Belastbarkeit des Widerstands in Watt. Hilft zu entscheiden, ob die
            Verlustleistung im zulässigen Bereich liegt.
        """
        if ohm <= 0:
            raise ValueError("Der Widerstandswert muss größer als Null sein.")

        self.ohm = ohm
        self.toleranz = toleranz
        self.leistung = leistung

    def berechne_strom(self, spannung: float) -> float:
        """Berechnet den Strom (in Ampere), der bei gegebener Spannung fließt.

        Ohmsches Gesetz: I = U / R.
        """
        return spannung / self.ohm

    def berechne_spannungsabfall(self, strom: float) -> float:
        """Berechnet die Spannung (in Volt), die bei gegebenem Strom abfällt."""
        return strom * self.ohm

    def liegt_wert_in_toleranz(self, messwert: float) -> bool:
        """Prüft, ob ein gemessener Widerstandswert innerhalb der Toleranz liegt."""
        untere_grenze = self.ohm * (1 - self.toleranz)
        obere_grenze = self.ohm * (1 + self.toleranz)
        return untere_grenze <= messwert <= obere_grenze

    def ist_leistung_ausreichend(self, spannung: float) -> bool:
        """Überprüft, ob der Widerstand die entstehende Verlustleistung aushält.

        Die Verlustleistung wird mit P = U^2 / R bestimmt.
        """
        verlustleistung = (spannung ** 2) / self.ohm
        return verlustleistung <= self.leistung

    def __repr__(self) -> str:
        """Liefert eine gut lesbare Darstellung für Studierende."""
        return (
            f"Widerstand({self.ohm:.0f} Ω, Toleranz ±{self.toleranz * 100:.0f} %, "
            f"Leistung {self.leistung:.2f} W)"
        )


if __name__ == "__main__":
    # Dieses Beispiel zeigt Schritt für Schritt, wie die Klasse genutzt wird.

    # Wir erzeugen einen Standard-Widerstand mit 220 Ohm, 5 % Toleranz und 0,25 W Leistung.
    standard_widerstand = Widerstand(ohm=220, toleranz=0.05, leistung=0.25)
    print("Erzeugte Instanz:", standard_widerstand)

    # Mit 5 Volt Eingangsspannung lässt sich der Strom berechnen.
    spannung = 5.0
    strom = standard_widerstand.berechne_strom(spannung)
    print(f"Bei {spannung} V fließen {strom:.3f} A.")

    # Umgekehrt berechnen wir den Spannungsabfall, wenn 0,01 A fließen sollen.
    zielstrom = 0.01
    spannungsabfall = standard_widerstand.berechne_spannungsabfall(zielstrom)
    print(f"Für {zielstrom:.3f} A benötigen wir {spannungsabfall:.2f} V.")

    # Studierende prüfen mit diesem Beispiel, ob ein gemessener Wert im Toleranzband liegt.
    gemessener_wert = 230
    print(
        f"Liegt {gemessener_wert} Ω innerhalb der Toleranz?",
        standard_widerstand.liegt_wert_in_toleranz(gemessener_wert),
    )

    # Schließlich kontrollieren wir, ob der Widerstand bei 12 V noch sicher ist.
    spannung_hoch = 12.0
    print(
        f"Hält der Widerstand {spannung_hoch} V aus?",
        standard_widerstand.ist_leistung_ausreichend(spannung_hoch),
    )
