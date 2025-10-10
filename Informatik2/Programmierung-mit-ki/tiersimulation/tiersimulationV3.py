# -*- coding: utf-8 -*-
# Diese Zeile ist eine sog. "Encoding-Deklaration": Sie sagt dem Python-Interpreter,
# dass die Datei in UTF-8 kodiert ist. Damit können Emojis/ü,ä,ö korrekt gelesen werden.

"""
Einfache 2D-Tiersimulation mit Tkinter-GUI.

Mehrzeiliger String (Docstring) ganz oben: beschreibt Zweck/Benutzung des Programms.
Wird nicht ausgeführt; dient als Dokumentation.
"""

from __future__ import annotations
# "from __future__ import annotations" bewirkt, dass Typannotationen (Type Hints)
# erst zur Laufzeit aufgelöst werden ("späte Bindung").
# Vorteil hier: Wir können den Typ "Welt" als String in Methoden verwenden,
# obwohl die Klasse "Welt" erst später im Code definiert wird.
# Ohne diesen Import müsste die Klasse bereits vorher bekannt sein.

import math
# Standardbibliothek "math": liefert mathematische Funktionen.
# Wir nutzen z. B. math.hypot(a, b), um Entfernungen (Pythagoras) zu berechnen.

import random
# Standardbibliothek "random": Zufallszahlen (für Startpositionen/Bewegungsrichtungen/Pflanzenwachstum).

import tkinter as tk
# "tkinter" ist die Standard-GUI-Bibliothek von Python.
# "as tk" gibt ihr einen kurzen Alias, damit wir z. B. tk.Tk(), tk.Canvas schreiben können.

from abc import ABC, abstractmethod
# "abc" = Abstract Base Classes.
# ABC: Basisklasse, von der wir erben, um eine abstrakte Klasse zu definieren.
# @abstractmethod: Dekorator, der eine Methode als "abstrakt" markiert,
# d. h. Unterklassen MÜSSEN diese Methode überschreiben.

from enum import Enum
# "Enum" ermöglicht Aufzählungstypen: feste, benannte Werte (z. B. PFLANZENFRESSER/FLEISCHFRESSER).

# =========================
#   Welt- und Darstellungs-Parameter
# =========================

GRID_W = 40
# Breite des Gitters (Anzahl Zellen in x-Richtung).

GRID_H = 22
# Höhe des Gitters (Anzahl Zellen in y-Richtung).

TILE = 24
# PIXELgröße einer Zelle im Canvas (jede Zelle ist 24x24 Pixel groß).

MARGIN = 8
# Rand in Pixeln um die gezeichnete Karte herum.

BG_COLOR = "#111418"
# Hintergrundfarbe des Fensters/Canvas (Hex-Farbcode).

PLANT_EMOJI = "🌿"
# Zeichen/Emoji, mit dem eine Pflanze dargestellt wird.

GRID_COLOR = "#263238"
# Farbe der Rasterlinien im Hintergrund.

TOOLTIP_BG = "#FFF3B0"
# Hintergrundfarbe der kleinen Info-Box (Tooltip).

TOOLTIP_FG = "#222"
# Textfarbe im Tooltip.

TEXT_FG = "#E0E6ED"
# Textfarbe der Statuszeile.

# =========================
#   Modellebene
# =========================

class Nahrung(Enum):
    # Definition eines Aufzählungstyps "Nahrung".
    # Vorteil: fixe, sichere Werte statt freier Strings (vermeidet Tippfehler).
    FLEISCHFRESSER = "Fleischfresser"
    # Enum-Wert mit internem Namen FLEISCHFRESSER und sichtbarem Text "Fleischfresser".
    PFLANZENFRESSER = "Pflanzenfresser"
    # Zweiter Enum-Wert.

class Tier(ABC):
    """
    Basisklasse für Tiere in der Simulation.
    "ABC" macht sie abstrakt: Von Tier direkt sollen keine Objekte erzeugt werden.
    Unterklassen (z. B. Loewe) erben und ergänzen fehlende Teile.
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
        # __init__ ist der KONSTRUKTOR: Er legt Startwerte für das Objekt fest.
        # name:          Anzeigename des Tiers (Typ: str = Zeichenkette).
        # nahrung:       Ernährungsart (Typ: Nahrung = Enum oben).
        # *,:            Das Sternchen vor dem Komma bewirkt: Alle folgenden Parameter
        #                müssen als "Keyword-Argumente" übergeben werden (z. B. x=1.0).
        # x, y:          Startposition in der Welt (Gleitkommazahlen für weiche Bewegung).
        # schrittweite:  Wie weit bewegt sich das Tier pro Tick maximal?
        # sichtweite:    Radius, in dem das Tier Futter/Beute wahrnimmt.
        # emoji:         Nur für die Darstellung; welches Symbol dieses Tier hat.

        self.name = name
        # "self" ist die Referenz auf das konkrete Objekt. Wir speichern den Namen im Objekt.

        self.nahrung = nahrung
        # Ernährungsart speichern (Enum).

        self.energie = 100
        # Startenergie. Wir begrenzen Energie später auf 0..100.

        self.x = x
        self.y = y
        # Startposition speichern.

        self.schrittweite = schrittweite
        # Maximale Bewegungsstrecke pro Tick.

        self.sichtweite = sichtweite
        # Wahrnehmungsradius für Suchen nach Pflanzen/Beute.

        self.emoji = emoji
        # Symbol für die Darstellung (GUI).

    # Alias mit Umlaut zur API aus deiner ursprünglichen Aufgabe
    def geräuschMachen(self):
        # Diese Methode mit Umlaut ruft die ASCII-Variante auf.
        return self.geraeusch_machen()

    @abstractmethod
    def geraeusch_machen(self) -> None: ...
    # @abstractmethod: Diese Methode HAT KEINE Implementierung hier.
    # "-> None" ist ein Type Hint für den Rückgabewert: Die Funktion soll nichts zurückgeben.
    # "None" ist in Python der spezielle Wert für "kein Wert".
    # "..." (Ellipsis) ist hier nur ein Platzhalter, bedeutet: "keine Funktionalität an dieser Stelle".

    @abstractmethod
    def essen(self) -> None: ...
    # Zweite abstrakte Methode: Unterklassen MÜSSEN definieren, wie "essen" Energie erhöht.

    def schlafen(self, stunden: int = 1) -> None:
        # Normale (konkrete) Methode: erhöht Energie abhängig von "stunden".
        # Parameter "stunden" hat Typ int und Standardwert 1.
        # Rückgabetyp "-> None": gibt nichts zurück.
        zuwachs = 15 * max(0, stunden)
        # Berechne Energiezuwachs: 15 pro Stunde; negative Stunden werden mit max(0, stunden) verhindert.
        self.energie = min(100, self.energie + zuwachs)
        # Kappe Energie bei 100 (Obergrenze).

    def bewegen(self, meter: float = 1.0) -> None:
        # Bewegung verbraucht Energie. Vereinfachtes Modell:
        verbrauch = max(1, int(meter // 2))
        # "meter // 2" = ganzzahlige Division; mindestens 1 Energiepunkt Verbrauch.
        self.energie = max(0, self.energie - verbrauch)
        # Untergrenze 0 (keine negative Energie).

    # Bewegungshelfer
    def _gehe_in_richtung(self, dx: float, dy: float, welt: "Welt" ) -> None:
        # PRIVATE Hilfsmethode (Unterstrich als Konvention): bewege dich in Richtung (dx,dy).
        # "welt: 'Welt'": Type Hint als STRING (wegen future annotations),
        # da Klasse Welt erst später kommt.
        dist = math.hypot(dx, dy)
        # Distanz der Richtungsvektors (Pythagoras): hypot(dx,dy) = sqrt(dx^2 + dy^2)

        if dist == 0:
            # Kein Richtungsvector -> keine Bewegung
            return

        f = self.schrittweite / dist
        # Skalierungsfaktor: so skalieren, dass die Bewegung genau "schrittweite" lang ist.

        nx, ny = self.x + dx * f, self.y + dy * f
        # Neue Zielposition berechnen.

        # Kantenabprall
        bounced = False
        # Merker, ob wir gegen eine Grenze geprallt sind (für Eventmeldung).

        if nx < 0:
            nx = -nx
            # Spiegelung an der linken Grenze: z. B. -0.3 -> +0.3
            bounced = True

        if ny < 0:
            ny = -ny
            # Spiegelung an der oberen Grenze.
            bounced = True

        if nx > welt.breite - 1:
            nx = (welt.breite - 1) - (nx - (welt.breite - 1))
            # Spiegelung an der rechten Grenze.
            bounced = True

        if ny > welt.hoehe - 1:
            ny = (welt.hoehe - 1) - (ny - (welt.hoehe - 1))
            # Spiegelung an der unteren Grenze.
            bounced = True

        self.x = max(0, min(welt.breite - 1, nx))
        self.y = max(0, min(welt.hoehe - 1, ny))
        # Sicherheitskappung: Stelle sicher, dass x,y im gültigen Bereich bleiben.

        self.bewegen(self.schrittweite)
        # Energieverbrauch für die Bewegung.

        if bounced and welt.on_event:
            welt.on_event(f"{self.name} prallt an der Grenze ab.")
            # Lose Kopplung: Wenn die Welt einen Ereignis-Callback hat (z. B. GUI),
            # dann eine Statusmeldung ausgeben.

    def _wandern(self, welt: "Welt") -> None:
        # Zufällige Bewegung ("Random Walk"):
        winkel = random.uniform(0, 2 * math.pi)
        # Zufallswinkel zwischen 0 und 2π (360 Grad).
        self._gehe_in_richtung(math.cos(winkel), math.sin(winkel), welt)
        # Bewegung entlang der Richtung, Normierung passiert in _gehe_in_richtung.

    def tick(self, welt: "Welt") -> None:
        # Ein "Tick" = ein Simulationsschritt für dieses Tier.
        if self.energie <= 0:
            # Tiere mit 0 Energie handeln nicht mehr.
            return

        if self.nahrung == Nahrung.PFLANZENFRESSER:
            self._tick_pflanzenfresser(welt)
        else:
            self._tick_fleischfresser(welt)
        # Polymorphes Verhalten: abhängig von der Ernährungsart andere Logik.

    def _tick_pflanzenfresser(self, welt: "Welt") -> None:
        # Verhalten für Pflanzenfresser:
        kachel = (round(self.x), round(self.y))
        # Runde Position auf Gitterkoordinate: eine Pflanze sitzt genau auf Zellen.
        if kachel in welt.pflanzen:
            # Steht auf einer Pflanze? -> essen
            welt.pflanzen.remove(kachel)
            # Pflanze aus der Welt entfernen (wurde "gefressen").
            self.essen()
            # Energie auffüllen gemäß Unterklassenlogik.
            if welt.on_event:
                welt.on_event(f"{self.name} weidet bei {kachel}.")
            return

        ziel = welt.naechste_pflanze(self.x, self.y, self.sichtweite)
        # Suche nach der nächsten Pflanze innerhalb der Sichtweite.
        if ziel is not None:
            zx, zy, d = ziel
            # Zielkoordinaten (Zelle) und Distanz.
            if d <= self.schrittweite:
                # Nah genug: direkt dorthin "springen".
                self.x, self.y = zx, zy
                self.bewegen(d)
                # Energieverbrauch proportional zur Distanz.
            else:
                # Sonst: in Richtung der Pflanze gehen (ein Schritt).
                self._gehe_in_richtung(zx - self.x, zy - self.y, welt)
        else:
            # Keine Pflanze gesehen:
            if self.energie < 40:
                self.schlafen(1)
                # Bei niedriger Energie kurz ausruhen.
            else:
                self._wandern(welt)
                # Sonst zufällig weiterziehen.

    def _tick_fleischfresser(self, welt: "Welt") -> None:
        # Verhalten für Fleischfresser:
        ziel = welt.naechster_pflanzenfresser(self, self.sichtweite)
        # Nächsten Pflanzenfresser suchen (siehe Welt-Methoden unten).
        if ziel is not None:
            beute, d = ziel
            if d <= 1.0:
                # Nah genug, um die Beute "zu erwischen".
                if beute in welt.tiere:
                    welt.tiere.remove(beute)
                    # Beute aus der Welt entfernen.
                    self.essen()
                    # Energie auffüllen.
                    if welt.on_event:
                        welt.on_event(f"{self.name} erlegt {beute.name}.")
                return
            else:
                # Noch nicht nah genug: bewege dich in Richtung Beute.
                self._gehe_in_richtung(beute.x - self.x, beute.y - self.y, welt)
        else:
            # Keine Beute in Sicht:
            if self.energie < 35:
                self.schlafen(1)
            else:
                self._wandern(welt)

# Konkrete Arten
class Loewe(Tier):
    # "Loewe" ERBT von "Tier": inherits Attribute/Methoden, überschreibt/ergänzt Spezifisches.
    def __init__(self, name: str, **kw):
        # Konstruktor ruft den Basisklassen-Konstruktor mit speziellen Standardwerten auf.
        super().__init__(name, Nahrung.FLEISCHFRESSER, schrittweite=1.2, sichtweite=8.0, emoji="🦁", **kw)
        # "super().__init__(...)" ruft den Konstruktor der Elternklasse (Tier).
        # **kw nimmt optionale benannte Argumente entgegen (z. B. x=..., y=...).
    def geraeusch_machen(self): pass
    # Überschreibt abstrakte Methode. "pass" = Platzhalter (keine Aktion, gültige leere Methode).
    def essen(self): self.energie = min(100, self.energie + 25)
    # Konkrete Umsetzung: Löwe gewinnt 25 Energie (gedeckelt bei 100).

class Nilpferd(Tier):
    def __init__(self, name: str, **kw):
        super().__init__(name, Nahrung.PFLANZENFRESSER, schrittweite=0.9, sichtweite=6.0, emoji="🦛", **kw)
    def geraeusch_machen(self): pass
    def essen(self): self.energie = min(100, self.energie + 22)

class Tiger(Tier):
    def __init__(self, name: str, **kw):
        super().__init__(name, Nahrung.FLEISCHFRESSER, schrittweite=1.3, sichtweite=8.0, emoji="🐯", **kw)
    def geraeusch_machen(self): pass
    def essen(self): self.energie = min(100, self.energie + 24)

class Hund(Tier):
    def __init__(self, name: str, **kw):
        super().__init__(name, Nahrung.FLEISCHFRESSER, schrittweite=1.1, sichtweite=7.0, emoji="🐕", **kw)
    def geraeusch_machen(self): pass
    def essen(self): self.energie = min(100, self.energie + 18)

class Katze(Tier):
    def __init__(self, name: str, **kw):
        super().__init__(name, Nahrung.FLEISCHFRESSER, schrittweite=1.0, sichtweite=6.5, emoji="🐈", **kw)
    def geraeusch_machen(self): pass
    def essen(self): self.energie = min(100, self.energie + 16)

class Wolf(Tier):
    def __init__(self, name: str, **kw):
        super().__init__(name, Nahrung.FLEISCHFRESSER, schrittweite=1.2, sichtweite=8.0, emoji="🐺", **kw)
    def geraeusch_machen(self): pass
    def essen(self): self.energie = min(100, self.energie + 20)

# Hinweis: Die sechs Unterklassen folgen demselben Muster:
# - super().__init__(...) setzt art-spezifische Standardwerte (schrittweite/sichtweite/emoji/nahrung).
# - geraeusch_machen: als Platzhalter implementiert (könnte man mit Sound/Text füllen).
# - essen: unterscheidet sich pro Art in der Energiemenge.

class Welt:
    """
    Eine einfache 2D-Welt.
    Hält Größe, Pflanzen (als Koordinaten-Set), Tiere (als Liste) und ein optionales Ereignis-Callback.
    Steuert die Simulation über die Methode tick().
    """
    def __init__(self, breite: int, hoehe: int, samen: int | None = 7):
        # Konstruktor der Welt.
        self.breite = breite
        # Anzahl Zellen horizontal.

        self.hoehe = hoehe
        # Anzahl Zellen vertikal.

        if samen is not None:
            random.seed(samen)
            # "Seed" für Zufallszahlen: gleiche Startwerte -> reproduzierbares Verhalten (nützlich für Tests/Demos).

        self.pflanzen: set[tuple[int, int]] = set()
        # Set von Pflanzen-Positionen (jede Pflanze sitzt auf einer Gitterzelle).
        # Type Hint "set[tuple[int,int]]": Menge von Tupeln (x,y).

        self.tiere: list[Tier] = []
        # Liste aller Tiere in der Welt (Type Hint: list[Tier]).

        self.on_event: callable | None = None
        # Optionaler Callback (Funktion), den die GUI setzen kann, um Statusmeldungen zu empfangen.
        # "callable | None": Entweder eine aufrufbare Funktion ODER None (kein Callback gesetzt).

    def add_pflanzen_random(self, anzahl: int) -> None:
        # Füge "anzahl" Pflanzen an zufälligen Positionen hinzu.
        for _ in range(anzahl):
            self.pflanzen.add((random.randrange(self.breite), random.randrange(self.hoehe)))
            # random.randrange(n) liefert eine Zufallszahl 0..n-1.

    def regrow_pflanzen(self, chance_pro_tick: float = 0.06) -> None:
        # Mit einer bestimmten Chance wächst pro Tick eine neue Pflanze irgendwo.
        if random.random() < chance_pro_tick:
            # random.random() gibt Zahl in [0.0, 1.0).
            self.pflanzen.add((random.randrange(self.breite), random.randrange(self.hoehe)))

    def add_tier(self, tier: Tier, x: float | None = None, y: float | None = None) -> None:
        # Tier hinzufügen. Falls keine Position vorgegeben, wähle zufällige.
        tier.x = random.uniform(0, self.breite - 1) if x is None else x
        # random.uniform(a,b): Gleitkomma-Zahl in [a,b].
        tier.y = random.uniform(0, self.hoehe - 1) if y is None else y
        self.tiere.append(tier)

    def naechste_pflanze(self, x: float, y: float, max_dist: float):
        # Suche die NÄCHSTE Pflanze innerhalb von "max_dist".
        # Einfacher Algorithmus: gehe alle Pflanzen durch und merke die beste (kleinsten Abstand).
        best = None
        for (px, py) in self.pflanzen:
            d = math.hypot(px - x, py - y)
            # Abstand zwischen Tierposition (x,y) und Pflanze (px,py).
            if d <= max_dist and (best is None or d < best[2]):
                # Nur Pflanzen innerhalb der Sichtweite beachten.
                # best ist ein Tupel (px, py, dist) -> best[2] ist die bisher beste Distanz.
                best = (px, py, d)
        return best
        # Rückgabe entweder None (keine in Reichweite) oder (x,y,dist).

    def naechster_pflanzenfresser(self, jaeger: Tier, max_dist: float):
        # Suche den nächsten Pflanzenfresser (für Fleischfresser).
        best = None
        for t in self.tiere:
            if t is jaeger or t.nahrung != Nahrung.PFLANZENFRESSER:
                # Sich selbst ignorieren und nur Pflanzenfresser betrachten.
                continue
            d = math.hypot(t.x - jaeger.x, t.y - jaeger.y)
            if d <= max_dist and (best is None or d < best[1]):
                # best hier als (Tier, Distanz) gespeichert -> best[1] ist Distanz.
                best = (t, d)
        return best
        # Rückgabe entweder None oder (TierObjekt, Distanz).

    def tick(self) -> None:
        # Ein Simulationsschritt für die gesamte Welt:
        random.shuffle(self.tiere)
        # Reihenfolge zufällig mischen (Fairness: nicht immer dieselbe Reihenfolge).

        lebende = list(self.tiere)
        # Kopie der Liste, damit wir sicher iterieren können,
        # auch wenn während des Ticks Tiere aus self.tiere entfernt werden (Beute).

        for t in lebende:
            if t in self.tiere:
                # Prüfen, ob Tier noch existiert (könnte bereits gefressen sein).
                t.tick(self)
                # Das einzelne Tier führt seinen Tick aus.

        self.regrow_pflanzen()
        # Chance auf Nachwachsen einer Pflanze.

# =========================
#   GUI-Schicht
# =========================

class App:
    # Klasse "App" bündelt GUI (View) und Steuerung (Controller).
    def __init__(self, root: tk.Tk):
        # Konstruktor: bekommt das Tk-Hauptfenster "root".
        self.root = root
        root.title("Tiersimulation – Tkinter")
        # Fenstertitel setzen.

        self.world = Welt(GRID_W, GRID_H, samen=7)
        # Erzeuge die Modell-Welt (Model) mit fixer Größe und Zufalls-Seed 7.

        self._setup_world()
        # Fülle die Welt mit Pflanzen und Tieren (Startzustand).

        # UI
        self.canvas_w = GRID_W * TILE + 2 * MARGIN
        # Breite des Zeichenbereichs in Pixeln.

        self.canvas_h = GRID_H * TILE + 2 * MARGIN
        # Höhe des Zeichenbereichs in Pixeln.

        self.canvas = tk.Canvas(root, width=self.canvas_w, height=self.canvas_h, bg=BG_COLOR, highlightthickness=0)
        # Canvas ist die Zeichenfläche für Raster, Pflanzen und Tiere.

        self.canvas.grid(row=0, column=0, columnspan=4, padx=8, pady=8)
        # Platziere das Canvas in einem einfachen Grid-Layout (Zeile 0, vier Spalten breit).

        # Steuerleiste
        self.btn_start = tk.Button(root, text="Start", command=self.start)
        # Button "Start": Beim Klicken wird self.start() aufgerufen.

        self.btn_pause = tk.Button(root, text="Pause", command=self.pause)
        # Button "Pause": Ruft self.pause().

        self.btn_slower = tk.Button(root, text="⟲ Langsamer", command=self.slower)
        # Button "Langsamer": vergrößert die Tick-Verzögerung.

        self.btn_faster = tk.Button(root, text="Schneller ⟳", command=self.faster)
        # Button "Schneller": verkleinert die Tick-Verzögerung.

        self.btn_start.grid(row=1, column=0, sticky="ew", padx=8, pady=(0,8))
        self.btn_pause.grid(row=1, column=1, sticky="ew", padx=8, pady=(0,8))
        self.btn_slower.grid(row=1, column=2, sticky="ew", padx=8, pady=(0,8))
        self.btn_faster.grid(row=1, column=3, sticky="ew", padx=8, pady=(0,8))
        # Anordnung der Buttons in der zweiten Zeile (row=1) nebeneinander.

        # Eventlabel
        self.event_var = tk.StringVar(value="Bereit.")
        # StringVar ist eine Tkinter-Variable, die an Widgets gebunden werden kann (Datenbindung).

        self.event_label = tk.Label(root, textvariable=self.event_var, fg=TEXT_FG, bg=BG_COLOR, anchor="w")
        # Label zeigt die aktuelle Statusnachricht an (verwendet textvariable).

        self.event_label.grid(row=2, column=0, columnspan=4, sticky="ew", padx=8, pady=(0,8))
        # Label unter den Buttons über die volle Breite.

        # Click-Handling
        self.canvas.bind("<Button-1>", self.on_click)
        # Mauslinksklicks auf dem Canvas werden an die Methode on_click übergeben (Controller).

        # Welt -> GUI Eventbrücke
        self.world.on_event = self.set_event
        # Setze den Ereignis-Callback der Welt auf die GUI-Methode set_event,
        # damit Domänenereignisse (z. B. "prallt an der Grenze ab") im Label landen.

        # Renderstate
        self.running = False
        # Merker, ob die Simulation läuft.

        self.delay_ms = 120
        # Startverzögerung zwischen Ticks in Millisekunden (Tempo).

        self.tooltip_id: int | None = None
        # Speichert die ID des zuletzt gezeichneten Tooltip-Rechtecks (oder None, wenn keiner sichtbar ist).
        # Type Hint "int | None" = entweder eine Canvas-ID (int) oder kein Tooltip.

        self.draw_static_grid()
        # Zeichne das Raster 1x (bleibt als Hintergrund bestehen).

        self.render()
        # Zeichne den ersten dynamischen Frame.

    def _setup_world(self):
        # Private Hilfsmethode: Startzustand der Welt konfigurieren.
        self.world.add_pflanzen_random(anzahl=100)
        # 100 Pflanzen zufällig verteilen.

        # Tiere
        self.world.add_tier(Loewe("Simba"))
        # Tierobjekt erstellen und in die Welt einfügen. Position wird zufällig gesetzt (keine x,y übergeben).
        self.world.add_tier(Tiger("ShereKhan"))
        self.world.add_tier(Wolf("Akela"))
        self.world.add_tier(Hund("Bello"))
        self.world.add_tier(Katze("Minka"))
        self.world.add_tier(Loewe("Willi"))
        self.world.add_tier(Tiger("Bernd"))
        self.world.add_tier(Wolf("Andre"))
        self.world.add_tier(Hund("Wuffi"))
        self.world.add_tier(Katze("Tetzi"))
        # Die obigen Zeilen wiederholen das Muster: Erzeuge Unterklassen von Tier mit Namen, füge sie hinzu.

        self.world.add_tier(Katze("mimi"))
        self.world.add_tier(Nilpferd("Wolle"))
        for i in range(3):
            self.world.add_tier(Nilpferd(f"Hippo{i+1}"))
        # Schleife: drei weitere Nilpferde mit Namen "Hippo1", "Hippo2", "Hippo3".

    # -------- Darstellung --------

    def grid_to_px(self, gx: float, gy: float) -> tuple[int, int]:
        # Hilfsfunktion: Wandle Gitterkoordinate (Zelle) in Pixel-Koordinate (Canvas) um.
        """Weltkoordinaten -> Pixel (Zellmitte)."""
        x = int(MARGIN + gx * TILE + TILE/2)
        y = int(MARGIN + gy * TILE + TILE/2)
        return x, y

    def draw_static_grid(self):
        # Zeichne das Raster (nur Linien). Bleibt als "Hintergrund".
        # Rasterlinien dezent
        for cx in range(GRID_W + 1):
            x = MARGIN + cx * TILE
            self.canvas.create_line(x, MARGIN, x, MARGIN + GRID_H * TILE, fill=GRID_COLOR)
        for cy in range(GRID_H + 1):
            y = MARGIN + cy * TILE
            self.canvas.create_line(MARGIN, y, MARGIN + GRID_W * TILE, y, fill=GRID_COLOR)

    def render(self):
        # Zeichne die dynamische Ebene neu (Pflanzen, Tiere, Tooltip).
        # dynamische Ebene löschen (behalte Raster)
        self.canvas.delete("dyn")
        # "tags=('dyn', ...)" markieren dynamische Elemente; hier werden sie entfernt.

        # Pflanzen zeichnen
        for (px, py) in self.world.pflanzen:
            cx, cy = self.grid_to_px(px, py)
            self.canvas.create_text(cx, cy, text=PLANT_EMOJI, tags=("dyn",), font=("Segoe UI Emoji", int(TILE*0.8)))

        # Tiere zeichnen
        for t in self.world.tiere:
            cx, cy = self.grid_to_px(t.x, t.y)
            self.canvas.create_text(
                cx, cy, text=t.emoji, tags=("dyn", f"tier"), font=("Segoe UI Emoji", int(TILE*0.9))
            )

        # Optional: Tooltip vorne halten
        if self.tooltip_id is not None:
            self.canvas.tag_raise(self.tooltip_id)
            # Bringt den Tooltip in der Zeichenreihenfolge nach vorn.

    # -------- Steuerung --------

    def start(self):
        # Startet die Simulationsschleife (falls nicht schon laufend).
        if not self.running:
            self.running = True
            self.loop()

    def pause(self):
        # Stoppt die Simulationsschleife.
        self.running = False

    def slower(self):
        # Verlangsamt das Tempo (erhöht die Wartezeit pro Frame).
        self.delay_ms = min(1000, int(self.delay_ms * 1.3))
        self.set_event(f"Tempo: {self.delay_ms} ms/Tick")

    def faster(self):
        # Beschleunigt das Tempo (verkleinert die Wartezeit pro Frame).
        self.delay_ms = max(15, int(self.delay_ms / 1.3))
        self.set_event(f"Tempo: {self.delay_ms} ms/Tick")

    def loop(self):
        # Hauptschleife der Simulation: wird immer wieder per Timer aufgerufen.
        if not self.running:
            return
        self.world.tick()
        # Model aktualisieren (ein Simulationsschritt).

        self.render()
        # Neu zeichnen (View).

        self.root.after(self.delay_ms, self.loop)
        # Timer: ruft self.loop() nach delay_ms Millisekunden wieder auf (Echtzeitgefühl).

    def set_event(self, msg: str):
        # Aktualisiert die Statuszeile (unten).
        self.event_var.set(msg)

    # -------- Interaktion --------

    def on_click(self, ev):
        # Ereignis-Handler für Mausklicks auf dem Canvas.
        # Nächstes Tier zur Klickposition finden
        # Umrechnen Pixel->Weltgrobe Koordinate
        wx = (ev.x - MARGIN) / TILE
        wy = (ev.y - MARGIN) / TILE

        best = None
        for t in self.world.tiere:
            d = math.hypot(t.x - wx, t.y - wy)
            # Abstand in Weltkoordinaten.
            if best is None or d < best[1]:
                best = (t, d)

        if best is None or best[1] > 1.2:
            # Wenn kein Tier in der Nähe (Schwelle 1.2 Zellen), Tooltip ausblenden.
            self.hide_tooltip()
            return

        t = best[0]
        txt = f"{t.name} ({t.nahrung.value})\nEnergie: {t.energie}"
        # Text für Tooltip mit Name, Ernährungsart (value aus Enum) und Energie.
        self.show_tooltip(ev.x, ev.y, txt)

    def show_tooltip(self, px: int, py: int, text: str, ttl_ms: int = 1500):
        # Zeichnet eine kleine Info-Box (Text + Hintergrund-Rechteck) am Klickpunkt.
        self.hide_tooltip()
        # Evtl. alten Tooltip entfernen.

        pad = 6
        # Innenabstand (Padding) im Tooltip.

        # Text
        tid = self.canvas.create_text(px, py, text=text, anchor="nw", fill=TOOLTIP_FG, font=("Segoe UI", 10), tags=("dyn",))
        # create_text gibt eine Canvas-ID zurück (hier in "tid").

        bbox = self.canvas.bbox(tid)
        # Bounding Box (x0,y0,x1,y1) des soeben gezeichneten Textes abfragen.

        if bbox is None:
            # Sicherheitsabfrage: sollte hier nicht passieren.
            return

        x0, y0, x1, y1 = bbox
        # Koordinaten der Box entpacken.

        # Hintergrund
        rect = self.canvas.create_rectangle(x0 - pad, y0 - pad, x1 + pad, y1 + pad, fill=TOOLTIP_BG, outline="#D5C48C", tags=("dyn",))
        # Rechteck hinter den Text zeichnen (leicht größer für Rand).

        # Z-Reihenfolge: Rechteck hinter Text
        self.canvas.tag_lower(rect, tid)
        # Schiebt das Rechteck hinter den Text (damit Text sichtbar bleibt).

        # Merken, damit wir es nach vorne holen/entfernen können
        self.tooltip_id = rect
        # Speichern die ID des Rechtecks (Tooltip besteht grafisch aus Rechteck+Text).

        self.canvas.after(ttl_ms, self.hide_tooltip)
        # Tooltip nach ttl_ms Millisekunden automatisch wieder entfernen.

    def hide_tooltip(self):
        # Entfernt den Tooltip, indem wir den Merker löschen und neu rendern.
        if self.tooltip_id is not None:
            # Lösche alle "dyn" Elemente reicht nicht; nur Tooltipelemente entfernen:
            # Wir löschen einfach und zeichnen frame neu.
            self.tooltip_id = None
            self.render()

def main():
    # Haupteinstiegspunkt, wenn die Datei direkt ausgeführt wird.
    root = tk.Tk()
    # Erzeuge das Tkinter-Hauptfenster.

    # Dunkles UI-Fenster
    try:
        root.configure(bg=BG_COLOR)
        # Setze die Hintergrundfarbe des Fensters (nicht auf allen Systemen verfügbar).
    except tk.TclError:
        # Falls die Plattform das nicht unterstützt, ignoriere den Fehler.
        pass

    app = App(root)
    # Erzeuge die App (GUI + Welt).

    root.mainloop()
    # Starte die Tkinter-Ereignisschleife (Programm bleibt hier "am Leben",
    # verarbeitet Events, bis das Fenster geschlossen wird).

if __name__ == "__main__":
    # Diese Bedingung ist in Python üblich:
    # Sie ist nur wahr, wenn die Datei direkt gestartet wurde (nicht importiert).
    main()
    # In diesem Fall rufen wir den Programmeinstieg "main()" auf.