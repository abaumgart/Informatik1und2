# -*- coding: utf-8 -*-
"""
Einfache 2D-Tiersimulation mit Tkinter-GUI.

- Welt: Raster aus Zellen; Pflanzen wachsen zufällig nach.
- Tiere: bewegen sich kontinuierlich, Fleischfresser jagen Pflanzenfresser.
- Darstellung: Pflanzen als 🌿, Tiere als Emojis auf einem Canvas.
- Bedienung: Start/Pause, schneller/langsamer. Klick auf ein Tier -> Tooltip.

Getestet mit Python 3.10+.
"""

from __future__ import annotations
import math
import random
import tkinter as tk
from abc import ABC, abstractmethod
from enum import Enum

# =========================
#   Welt- und Darstellungs-Parameter
# =========================

GRID_W = 40
GRID_H = 22
TILE = 24                  # Pixel pro Zelle
MARGIN = 8                 # Rand um die Karte herum
BG_COLOR = "#111418"

PLANT_EMOJI = "🌿"
GRID_COLOR = "#263238"
TOOLTIP_BG = "#FFF3B0"
TOOLTIP_FG = "#222"
TEXT_FG = "#E0E6ED"

# =========================
#   Modellebene
# =========================

class Nahrung(Enum):
    FLEISCHFRESSER = "Fleischfresser"
    PFLANZENFRESSER = "Pflanzenfresser"


class Tier(ABC):
    """
    Basisklasse für Tiere in der Simulation.
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
        self.name = name
        self.nahrung = nahrung
        self.energie = 100
        self.x = x
        self.y = y
        self.schrittweite = schrittweite
        self.sichtweite = sichtweite
        self.emoji = emoji

    # Alias mit Umlaut zur API aus deiner ursprünglichen Aufgabe
    def geräuschMachen(self):
        return self.geraeusch_machen()

    @abstractmethod
    def geraeusch_machen(self) -> None: ...
    @abstractmethod
    def essen(self) -> None: ...

    def schlafen(self, stunden: int = 1) -> None:
        zuwachs = 15 * max(0, stunden)
        self.energie = min(100, self.energie + zuwachs)

    def bewegen(self, meter: float = 1.0) -> None:
        verbrauch = max(1, int(meter // 2))
        self.energie = max(0, self.energie - verbrauch)

    # Bewegungshelfer
    def _gehe_in_richtung(self, dx: float, dy: float, welt: "Welt") -> None:
        dist = math.hypot(dx, dy)
        if dist == 0:
            return
        f = self.schrittweite / dist
        nx, ny = self.x + dx * f, self.y + dy * f

        # Kantenabprall
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

        self.x = max(0, min(welt.breite - 1, nx))
        self.y = max(0, min(welt.hoehe - 1, ny))
        self.bewegen(self.schrittweite)
        if bounced and welt.on_event:
            welt.on_event(f"{self.name} prallt an der Grenze ab.")

    def _wandern(self, welt: "Welt") -> None:
        winkel = random.uniform(0, 2 * math.pi)
        self._gehe_in_richtung(math.cos(winkel), math.sin(winkel), welt)

    def tick(self, welt: "Welt") -> None:
        if self.energie <= 0:
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
            if welt.on_event:
                welt.on_event(f"{self.name} weidet bei {kachel}.")
            return

        ziel = welt.naechste_pflanze(self.x, self.y, self.sichtweite)
        if ziel is not None:
            zx, zy, d = ziel
            if d <= self.schrittweite:
                self.x, self.y = zx, zy
                self.bewegen(d)
            else:
                self._gehe_in_richtung(zx - self.x, zy - self.y, welt)
        else:
            if self.energie < 40:
                self.schlafen(1)
            else:
                self._wandern(welt)

    def _tick_fleischfresser(self, welt: "Welt") -> None:
        ziel = welt.naechster_pflanzenfresser(self, self.sichtweite)
        if ziel is not None:
            beute, d = ziel
            if d <= 1.0:
                if beute in welt.tiere:
                    welt.tiere.remove(beute)
                    self.essen()
                    if welt.on_event:
                        welt.on_event(f"{self.name} erlegt {beute.name}.")
                return
            else:
                self._gehe_in_richtung(beute.x - self.x, beute.y - self.y, welt)
        else:
            if self.energie < 35:
                self.schlafen(1)
            else:
                self._wandern(welt)


# Konkrete Arten
class Loewe(Tier):
    def __init__(self, name: str, **kw):
        super().__init__(name, Nahrung.FLEISCHFRESSER, schrittweite=1.2, sichtweite=8.0, emoji="🦁", **kw)
    def geraeusch_machen(self): pass
    def essen(self): self.energie = min(100, self.energie + 25)

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


class Welt:
    """
    Eine einfache 2D-Welt.
    """
    def __init__(self, breite: int, hoehe: int, samen: int | None = 7):
        self.breite = breite
        self.hoehe = hoehe
        if samen is not None:
            random.seed(samen)
        self.pflanzen: set[tuple[int, int]] = set()
        self.tiere: list[Tier] = []
        self.on_event: callable | None = None  # GUI-Callback für Meldungen

    def add_pflanzen_random(self, anzahl: int) -> None:
        for _ in range(anzahl):
            self.pflanzen.add((random.randrange(self.breite), random.randrange(self.hoehe)))

    def regrow_pflanzen(self, chance_pro_tick: float = 0.06) -> None:
        if random.random() < chance_pro_tick:
            self.pflanzen.add((random.randrange(self.breite), random.randrange(self.hoehe)))

    def add_tier(self, tier: Tier, x: float | None = None, y: float | None = None) -> None:
        tier.x = random.uniform(0, self.breite - 1) if x is None else x
        tier.y = random.uniform(0, self.hoehe - 1) if y is None else y
        self.tiere.append(tier)

    def naechste_pflanze(self, x: float, y: float, max_dist: float):
        best = None
        for (px, py) in self.pflanzen:
            d = math.hypot(px - x, py - y)
            if d <= max_dist and (best is None or d < best[2]):
                best = (px, py, d)
        return best

    def naechster_pflanzenfresser(self, jaeger: Tier, max_dist: float):
        best = None
        for t in self.tiere:
            if t is jaeger or t.nahrung != Nahrung.PFLANZENFRESSER:
                continue
            d = math.hypot(t.x - jaeger.x, t.y - jaeger.y)
            if d <= max_dist and (best is None or d < best[1]):
                best = (t, d)
        return best

    def tick(self) -> None:
        random.shuffle(self.tiere)
        lebende = list(self.tiere)
        for t in lebende:
            if t in self.tiere:
                t.tick(self)
        self.regrow_pflanzen()


# =========================
#   GUI-Schicht
# =========================

class App:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("Tiersimulation – Tkinter")

        self.world = Welt(GRID_W, GRID_H, samen=7)
        self._setup_world()

        # UI
        self.canvas_w = GRID_W * TILE + 2 * MARGIN
        self.canvas_h = GRID_H * TILE + 2 * MARGIN
        self.canvas = tk.Canvas(root, width=self.canvas_w, height=self.canvas_h, bg=BG_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=4, padx=8, pady=8)

        # Steuerleiste
        self.btn_start = tk.Button(root, text="Start", command=self.start)
        self.btn_pause = tk.Button(root, text="Pause", command=self.pause)
        self.btn_slower = tk.Button(root, text="⟲ Langsamer", command=self.slower)
        self.btn_faster = tk.Button(root, text="Schneller ⟳", command=self.faster)

        self.btn_start.grid(row=1, column=0, sticky="ew", padx=8, pady=(0,8))
        self.btn_pause.grid(row=1, column=1, sticky="ew", padx=8, pady=(0,8))
        self.btn_slower.grid(row=1, column=2, sticky="ew", padx=8, pady=(0,8))
        self.btn_faster.grid(row=1, column=3, sticky="ew", padx=8, pady=(0,8))

        # Eventlabel
        self.event_var = tk.StringVar(value="Bereit.")
        self.event_label = tk.Label(root, textvariable=self.event_var, fg=TEXT_FG, bg=BG_COLOR, anchor="w")
        self.event_label.grid(row=2, column=0, columnspan=4, sticky="ew", padx=8, pady=(0,8))

        # Click-Handling
        self.canvas.bind("<Button-1>", self.on_click)

        # Welt -> GUI Eventbrücke
        self.world.on_event = self.set_event

        # Renderstate
        self.running = False
        self.delay_ms = 120  # anfängliche Tickdauer
        self.tooltip_id: int | None = None

        self.draw_static_grid()
        self.render()  # initialer Frame

    def _setup_world(self):
        self.world.add_pflanzen_random(anzahl=10)
        # Tiere
        self.world.add_tier(Loewe("Simba"))
        self.world.add_tier(Tiger("ShereKhan"))
        self.world.add_tier(Wolf("Akela"))
        self.world.add_tier(Hund("Bello"))
        self.world.add_tier(Katze("Minka"))
        self.world.add_tier(Loewe("Willi"))
        self.world.add_tier(Tiger("Bernd"))
        self.world.add_tier(Wolf("Andre"))
        self.world.add_tier(Hund("Wuffi"))
        self.world.add_tier(Katze("Tetzi"))
        
        self.world.add_tier(Katze("mimi"))
        self.world.add_tier(Nilpferd("Wolle"))
        for i in range(3):
            self.world.add_tier(Nilpferd(f"Hippo{i+1}"))

    # -------- Darstellung --------

    def grid_to_px(self, gx: float, gy: float) -> tuple[int, int]:
        """Weltkoordinaten -> Pixel (Zellmitte)."""
        x = int(MARGIN + gx * TILE + TILE/2)
        y = int(MARGIN + gy * TILE + TILE/2)
        return x, y

    def draw_static_grid(self):
        # Rasterlinien dezent
        for cx in range(GRID_W + 1):
            x = MARGIN + cx * TILE
            self.canvas.create_line(x, MARGIN, x, MARGIN + GRID_H * TILE, fill=GRID_COLOR)
        for cy in range(GRID_H + 1):
            y = MARGIN + cy * TILE
            self.canvas.create_line(MARGIN, y, MARGIN + GRID_W * TILE, y, fill=GRID_COLOR)

    def render(self):
        # dynamische Ebene löschen (behalte Raster)
        self.canvas.delete("dyn")

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

    # -------- Steuerung --------

    def start(self):
        if not self.running:
            self.running = True
            self.loop()

    def pause(self):
        self.running = False

    def slower(self):
        self.delay_ms = min(1000, int(self.delay_ms * 1.3))
        self.set_event(f"Tempo: {self.delay_ms} ms/Tick")

    def faster(self):
        self.delay_ms = max(15, int(self.delay_ms / 1.3))
        self.set_event(f"Tempo: {self.delay_ms} ms/Tick")

    def loop(self):
        if not self.running:
            return
        self.world.tick()
        self.render()
        self.root.after(self.delay_ms, self.loop)

    def set_event(self, msg: str):
        self.event_var.set(msg)

    # -------- Interaktion --------

    def on_click(self, ev):
        # Nächstes Tier zur Klickposition finden
        # Umrechnen Pixel->Weltgrobe Koordinate
        wx = (ev.x - MARGIN) / TILE
        wy = (ev.y - MARGIN) / TILE

        best = None
        for t in self.world.tiere:
            d = math.hypot(t.x - wx, t.y - wy)
            if best is None or d < best[1]:
                best = (t, d)

        if best is None or best[1] > 1.2:
            self.hide_tooltip()
            return

        t = best[0]
        txt = f"{t.name} ({t.nahrung.value})\nEnergie: {t.energie}"
        self.show_tooltip(ev.x, ev.y, txt)

    def show_tooltip(self, px: int, py: int, text: str, ttl_ms: int = 1500):
        self.hide_tooltip()
        pad = 6
        # Text
        tid = self.canvas.create_text(px, py, text=text, anchor="nw", fill=TOOLTIP_FG, font=("Segoe UI", 10), tags=("dyn",))
        bbox = self.canvas.bbox(tid)
        if bbox is None:
            return
        x0, y0, x1, y1 = bbox
        # Hintergrund
        rect = self.canvas.create_rectangle(x0 - pad, y0 - pad, x1 + pad, y1 + pad, fill=TOOLTIP_BG, outline="#D5C48C", tags=("dyn",))
        # Z-Reihenfolge: Rechteck hinter Text
        self.canvas.tag_lower(rect, tid)
        # Merken, damit wir es nach vorne holen/entfernen können
        self.tooltip_id = rect
        self.canvas.after(ttl_ms, self.hide_tooltip)

    def hide_tooltip(self):
        if self.tooltip_id is not None:
            # Lösche alle "dyn" Elemente reicht nicht; nur Tooltipelemente entfernen:
            # Wir löschen einfach und zeichnen frame neu.
            self.tooltip_id = None
            self.render()


def main():
    root = tk.Tk()
    # Dunkles UI-Fenster
    try:
        root.configure(bg=BG_COLOR)
    except tk.TclError:
        pass
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()