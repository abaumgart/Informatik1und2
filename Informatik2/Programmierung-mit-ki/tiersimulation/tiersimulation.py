# -*- coding: utf-8 -*-
from __future__ import annotations
import random
import math
from abc import ABC, abstractmethod
from enum import Enum

# =========================
#   Grundmodelle
# =========================

class Nahrung(Enum):
    FLEISCHFRESSER = "Fleischfresser"
    PFLANZENFRESSER = "Pflanzenfresser"


class Tier(ABC):
    """
    Basisklasse für Tiere in der Simulation.

    Attribute:
        name (str): Anzeigename.
        nahrung (Nahrung): Fleischfresser oder Pflanzenfresser.
        energie (int): 0..100
        x, y (float): Position in der Welt.
        schrittweite (float): Wieviel Meter/Tile pro Tick.
        sichtweite (float): Reichweite für Futtersuche / Jagd.
        emoji (str): Darstellung im Renderer.

    Fähigkeiten:
        geräuschMachen()  -> Alias für geraeusch_machen()
        essen()           -> art-spezifisch; erhöht Energie
        schlafen(stunden=1)
        bewegen(meter=1.0)
        tick(welt)        -> eine Simulationsentscheidung pro Tick
    """

    def __init__(
        self,
        name: str,
        nahrung: Nahrung,
        *,
        x: float = 0.0,
        y: float = 0.0,
        schrittweite: float = 1.0,
        sichtweite: float = 6.0,
        emoji: str = "?"
    ):
        if not isinstance(nahrung, Nahrung):
            raise ValueError("nahrung muss ein Wert der Nahrung-Enum sein.")
        self.name = name
        self.nahrung = nahrung
        self.energie = 100
        self.x = x
        self.y = y
        self.schrittweite = schrittweite
        self.sichtweite = sichtweite
        self.emoji = emoji

    # Alias mit Umlaut – bleibt zu deiner ursprünglichen API kompatibel
    def geräuschMachen(self):
        return self.geraeusch_machen()

    @abstractmethod
    def geraeusch_machen(self) -> None: ...
    @abstractmethod
    def essen(self) -> None: ...

    def schlafen(self, stunden: int = 1) -> None:
        zuwachs = 15 * max(stunden, 0)
        alt = self.energie
        self.energie = min(100, self.energie + zuwachs)
        print(f"{self.name} schläft {stunden}h ({alt}→{self.energie} Energie).")

    def bewegen(self, meter: float = 1.0) -> None:
        verbrauch = max(1, int(meter // 2))  # grobes Modell
        alt = self.energie
        self.energie = max(0, self.energie - verbrauch)
        # kein Print hier; Ausgabe übernimmt tick()
        # print(f"{self.name} bewegt sich {meter:.1f}m ({alt}→{self.energie}).")

    # Hilfsmethoden für Bewegung in 2D
    def _gehe_in_richtung(self, dx: float, dy: float, welt: "Welt") -> None:
        # normiere auf schrittweite
        dist = math.hypot(dx, dy)
        if dist == 0:
            return
        f = self.schrittweite / dist
        nx, ny = self.x + dx * f, self.y + dy * f

        # Abprallen an den Weltgrenzen
        bounced = False
        if nx < 0:
            nx = -nx
            bounced = True
        if ny < 0:
            ny = -ny
            bounced = True
        if nx > welt.breite - 1:
            nx = (welt.breite - 1) - (nx - (welt.breite - 1))
            bounced = True
        if ny > welt.hoehe - 1:
            ny = (welt.hoehe - 1) - (ny - (welt.hoehe - 1))
            bounced = True

        self.x, self.y = max(0, min(welt.breite - 1, nx)), max(0, min(welt.hoehe - 1, ny))
        self.bewegen(self.schrittweite)
        if bounced:
            print(f"{self.name} prallt an der Grenze ab.")

    def _wandern(self, welt: "Welt") -> None:
        # leichte Richtungsänderung
        winkel = random.uniform(0, 2 * math.pi)
        self._gehe_in_richtung(math.cos(winkel), math.sin(winkel), welt)

    # --- Kernlogik pro Tick ---
    def tick(self, welt: "Welt") -> None:
        if self.energie <= 0:
            print(f"{self.name} ist erschöpft und bewegt sich nicht.")
            return

        if self.nahrung == Nahrung.PFLANZENFRESSER:
            self._tick_pflanzenfresser(welt)
        else:
            self._tick_fleischfresser(welt)

    def _tick_pflanzenfresser(self, welt: "Welt") -> None:
        kachel = (round(self.x), round(self.y))
        if kachel in welt.pflanzen:
            welt.pflanzen.remove(kachel)
            self.essen()
            return

        ziel = welt.naechste_pflanze(self.x, self.y, self.sichtweite)
        if ziel is not None:
            zx, zy, d = ziel
            # Wenn nah dran, direkt hin
            if d <= self.schrittweite:
                self.x, self.y = zx, zy
                self.bewegen(d)
            else:
                self._gehe_in_richtung(zx - self.x, zy - self.y, welt)
            print(f"{self.name} sucht Futter (🌿 in Sichtweite).")
        else:
            # keine Pflanze in Sicht: Energiemanagement
            if self.energie < 40:
                self.schlafen(1)
            else:
                self._wandern(welt)

    def _tick_fleischfresser(self, welt: "Welt") -> None:
        ziel = welt.naechster_pflanzenfresser(self, self.sichtweite)
        if ziel is not None:
            beute, d = ziel
            if d <= 1.0:
                # Jagd erfolgreich
                if beute in welt.tiere:
                    welt.tiere.remove(beute)
                    print(f"{self.name} jagt {beute.name} (✅ gefangen).")
                    self.essen()
                return
            else:
                self._gehe_in_richtung(beute.x - self.x, beute.y - self.y, welt)
                print(f"{self.name} jagt {beute.name}.")
        else:
            if self.energie < 35:
                self.schlafen(1)
            else:
                self._wandern(welt)


# =========================
#   Konkrete Tierarten
# =========================

class Loewe(Tier):
    def __init__(self, name: str, **kw):
        super().__init__(name, Nahrung.FLEISCHFRESSER, schrittweite=1.2, sichtweite=8.0, emoji="🦁", **kw)
    def geraeusch_machen(self): print(f"{self.name}: Roooar!")
    def essen(self):
        alt = self.energie
        self.energie = min(100, self.energie + 25)
        print(f"{self.name} frisst Fleisch ({alt}→{self.energie} Energie).")

class Nilpferd(Tier):
    def __init__(self, name: str, **kw):
        super().__init__(name, Nahrung.PFLANZENFRESSER, schrittweite=0.9, sichtweite=6.0, emoji="🦛", **kw)
    def geraeusch_machen(self): print(f"{self.name}: Grunz! (tiefes Schnauben)")
    def essen(self):
        alt = self.energie
        self.energie = min(100, self.energie + 22)
        print(f"{self.name} frisst Wasserpflanzen ({alt}→{self.energie}).")

class Tiger(Tier):
    def __init__(self, name: str, **kw):
        super().__init__(name, Nahrung.FLEISCHFRESSER, schrittweite=1.3, sichtweite=8.0, emoji="🐯", **kw)
    def geraeusch_machen(self): print(f"{self.name}: Grrrr!")
    def essen(self):
        alt = self.energie
        self.energie = min(100, self.energie + 24)
        print(f"{self.name} frisst Fleisch ({alt}→{self.energie}).")

class Hund(Tier):
    def __init__(self, name: str, **kw):
        super().__init__(name, Nahrung.FLEISCHFRESSER, schrittweite=1.1, sichtweite=7.0, emoji="🐕", **kw)
    def geraeusch_machen(self): print(f"{self.name}: Wuff! Wuff!")
    def essen(self):
        alt = self.energie
        self.energie = min(100, self.energie + 18)
        print(f"{self.name} frisst Fleisch/Kroketten ({alt}→{self.energie}).")

class Katze(Tier):
    def __init__(self, name: str, **kw):
        super().__init__(name, Nahrung.FLEISCHFRESSER, schrittweite=1.0, sichtweite=6.5, emoji="🐈", **kw)
    def geraeusch_machen(self): print(f"{self.name}: Miau!")
    def essen(self):
        alt = self.energie
        self.energie = min(100, self.energie + 16)
        print(f"{self.name} frisst Fleisch ({alt}→{self.energie}).")

class Wolf(Tier):
    def __init__(self, name: str, **kw):
        super().__init__(name, Nahrung.FLEISCHFRESSER, schrittweite=1.2, sichtweite=8.0, emoji="🐺", **kw)
    def geraeusch_machen(self): print(f"{self.name}: Auuuu!")
    def essen(self):
        alt = self.energie
        self.energie = min(100, self.energie + 20)
        print(f"{self.name} frisst Fleisch (Rudelinstinkt) ({alt}→{self.energie}).")


# =========================
#   Welt / Simulation
# =========================

class Welt:
    """
    Eine einfache 2D-Welt mit gittriger Darstellung.

    - pflanzen: Set[(int,int)] mit Zellen, die Nahrung für Pflanzenfresser enthalten.
    - tiere: Liste aller Tierobjekte.
    """
    def __init__(self, breite: int = 40, hoehe: int = 20, samen: int | None = 42):
        self.breite = breite
        self.hoehe = hoehe
        if samen is not None:
            random.seed(samen)
        self.pflanzen: set[tuple[int,int]] = set()
        self.tiere: list[Tier] = []

    def add_pflanzen_random(self, anzahl: int) -> None:
        for _ in range(anzahl):
            self.pflanzen.add((random.randrange(self.breite), random.randrange(self.hoehe)))

    def add_tier(self, tier: Tier, x: float | None = None, y: float | None = None) -> None:
        tier.x = random.uniform(0, self.breite-1) if x is None else x
        tier.y = random.uniform(0, self.hoehe-1) if y is None else y
        self.tiere.append(tier)

    def naechste_pflanze(self, x: float, y: float, max_dist: float) -> tuple[int,int,float] | None:
        best = None
        for (px, py) in self.pflanzen:
            d = math.hypot(px - x, py - y)
            if d <= max_dist and (best is None or d < best[2]):
                best = (px, py, d)
        return best

    def naechster_pflanzenfresser(self, jaeger: Tier, max_dist: float) -> tuple[Tier,float] | None:
        best = None
        for t in self.tiere:
            if t is jaeger:
                continue
            if t.nahrung == Nahrung.PFLANZENFRESSER:
                d = math.hypot(t.x - jaeger.x, t.y - jaeger.y)
                if d <= max_dist and (best is None or d < best[1]):
                    best = (t, d)
        return best

    def regrow_pflanzen(self, chance_pro_tick: float = 0.06) -> None:
        # Jede freie Zelle hat eine kleine Chance, eine Pflanze zu spawnen
        if random.random() < chance_pro_tick:
            self.pflanzen.add((random.randrange(self.breite), random.randrange(self.hoehe)))

    def tick(self) -> None:
        # In zufälliger Reihenfolge agieren lassen (reduziert deterministische Beutevorteile)
        random.shuffle(self.tiere)
        # Snapshot, damit entfernte Tiere nicht mitten im Loop Probleme machen
        lebende = list(self.tiere)
        for t in lebende:
            if t in self.tiere:  # könnte von einem Räuber entfernt worden sein
                t.tick(self)
        self.regrow_pflanzen()

    # --- Anzeige (optional) ---
    def render(self) -> str:
        # Wir bauen ein Raster aus Unicode/Emoji
        raster = [["·" for _ in range(self.breite)] for _ in range(self.hoehe)]
        for (px, py) in self.pflanzen:
            if 0 <= px < self.breite and 0 <= py < self.hoehe:
                raster[py][px] = "🌿"

        # Tiere zeichnen (später zeichnen überdeckt Pflanzen optisch)
        for t in self.tiere:
            ix, iy = int(round(t.x)), int(round(t.y))
            if 0 <= ix < self.breite and 0 <= iy < self.hoehe:
                raster[iy][ix] = t.emoji

        return "\n".join("".join(zeile) for zeile in raster)


# =========================
#   Demo / Einstiegspunkt
# =========================

if __name__ == "__main__":
    welt = Welt(breite=40, hoehe=20, samen=7)
    welt.add_pflanzen_random(anzahl=60)

    # Tiere hinzufügen
    welt.add_tier(Loewe("Simba"))
    welt.add_tier(Tiger("ShereKhan"))
    welt.add_tier(Wolf("Akela"))
    welt.add_tier(Hund("Bello"))
    welt.add_tier(Katze("Minka"))
    welt.add_tier(Nilpferd("Hattie"))

    # ein paar zusätzliche Pflanzenfresser für Dynamik:
    for i in range(3):
        welt.add_tier(Nilpferd(f"Hippo{i+1}"))

    # Startgeräusche (rein zur Stimmung)
    for t in welt.tiere:
        t.geräuschMachen()

    TICKS = 50
    for tick in range(1, TICKS + 1):
        print(f"\n=== Tick {tick} ===")
        welt.tick()
        # alle 5 Ticks rendern
        if tick % 5 == 0 or tick == 1:
            print(welt.render())

    print("\nSimulation beendet.")