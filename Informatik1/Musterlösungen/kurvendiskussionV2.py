import tkinter as tk
from tkinter import ttk, messagebox

import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class PolynomOberflaeche:
    def __init__(self, hauptfenster):
        """Konstruktor: Hier wird die grafische Oberfläche aufgebaut."""
        self.hauptfenster = hauptfenster
        self.hauptfenster.title("Polynom-Tool mit Ableitungen")

        # Variablen für Eingaben
        self.grad_variable = tk.IntVar(value=3)       # Startwert: Grad 3
        self.x_min_variable = tk.DoubleVar(value=-10.0)
        self.x_max_variable = tk.DoubleVar(value=10.0)

        # Liste für die Eingabefelder der Koeffizienten
        self.koeffizienten_felder = []

        # Oberfläche aufbauen
        self.baue_layout()

    def baue_layout(self):
        """Legt die Anordnung der grafischen Elemente fest."""

        # Oberer Bereich für Steuerungselemente
        steuerung_rahmen = ttk.Frame(self.hauptfenster, padding=10)
        steuerung_rahmen.pack(side=tk.TOP, fill=tk.X)

        # Grad-Eingabe
        ttk.Label(steuerung_rahmen, text="Grad des Polynoms:").grid(row=0, column=0, sticky="w")
        ttk.Entry(steuerung_rahmen, textvariable=self.grad_variable, width=5).grid(row=0, column=1, padx=5)

        ttk.Button(
            steuerung_rahmen,
            text="Koeffizienten-Felder erzeugen",
            command=self.erzeuge_koeffizienten_felder
        ).grid(row=0, column=2, padx=10)

        # Bereich für x-Min und x-Max
        ttk.Label(steuerung_rahmen, text="x-Min:").grid(row=1, column=0, sticky="w", pady=(5, 0))
        ttk.Entry(steuerung_rahmen, textvariable=self.x_min_variable, width=7).grid(row=1, column=1, sticky="w", pady=(5, 0))

        ttk.Label(steuerung_rahmen, text="x-Max:").grid(row=1, column=2, sticky="w", pady=(5, 0))
        ttk.Entry(steuerung_rahmen, textvariable=self.x_max_variable, width=7).grid(row=1, column=3, sticky="w", pady=(5, 0))

        ttk.Button(
            steuerung_rahmen,
            text="Polynom und Ableitungen zeichnen",
            command=self.zeichne_polynom_und_ableitungen
        ).grid(row=0, column=3, padx=10)

        # Rahmen für die Koeffizienten-Eingabefelder
        self.koeffizienten_rahmen = ttk.LabelFrame(
            self.hauptfenster,
            text="Koeffizienten (a_n bis a_0)",
            padding=10
        )
        self.koeffizienten_rahmen.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        # Rahmen für den Plot
        plot_rahmen = ttk.Frame(self.hauptfenster, padding=10)
        plot_rahmen.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Matplotlib-Figur und Achse
        self.grafik = Figure(figsize=(6, 4))
        self.koordinaten_achse = self.grafik.add_subplot(111)
        self.koordinaten_achse.set_title("Polynom und Ableitungen")
        self.koordinaten_achse.set_xlabel("x")
        self.koordinaten_achse.set_ylabel("f(x)")
        self.koordinaten_achse.grid(True)

        # Canvas, damit die Matplotlib-Grafik in Tkinter angezeigt wird
        self.leinwand = FigureCanvasTkAgg(self.grafik, master=plot_rahmen)
        self.leinwand.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def erzeuge_koeffizienten_felder(self):
        """Erzeugt Eingabefelder für die Koeffizienten entsprechend dem Grad."""

        # Alte Eingabefelder entfernen
        for element in self.koeffizienten_rahmen.winfo_children():
            element.destroy()
        self.koeffizienten_felder = []

        grad = self.grad_variable.get()
        if grad < 0:
            messagebox.showerror("Fehler", "Der Grad des Polynoms muss mindestens 0 sein.")
            return

        ttk.Label(
            self.koeffizienten_rahmen,
            text="Bitte die Koeffizienten eingeben (von a_n bis a_0):"
        ).grid(row=0, column=0, columnspan=grad + 1, sticky="w", pady=(0, 5))

        # Eingabefelder von a_n bis a_0 erzeugen
        for spalte, exponent in enumerate(range(grad, -1, -1)):
            ttk.Label(self.koeffizienten_rahmen, text=f"a_{exponent}").grid(row=1, column=spalte, padx=5, pady=2)
            eingabefeld = ttk.Entry(self.koeffizienten_rahmen, width=7)
            eingabefeld.grid(row=2, column=spalte, padx=5, pady=2)
            eingabefeld.insert(0, "0.0")  # Standardwert
            self.koeffizienten_felder.append(eingabefeld)

    def lese_koeffizienten(self):
        """
        Liest die eingegebenen Koeffizienten aus den Eingabefeldern.
        Gibt ein NumPy-Array zurück, das die Koeffizienten enthält.
        Reihenfolge: [a_n, ..., a_0]
        """
        if not self.koeffizienten_felder:
            messagebox.showerror("Fehler", "Bitte erzeugen Sie zuerst die Koeffizienten-Felder.")
            return None

        koeffizienten_liste = []

        try:
            for eingabefeld in self.koeffizienten_felder:
                wert = float(eingabefeld.get())
                koeffizienten_liste.append(wert)
        except ValueError:
            messagebox.showerror("Fehler", "Bitte geben Sie nur gültige Zahlen für die Koeffizienten ein.")
            return None

        koeffizienten_array = np.array(koeffizienten_liste)
        return koeffizienten_array

    def zeichne_polynom_und_ableitungen(self):
        """
        Liest die Koeffizienten ein, berechnet das Polynom,
        die erste und zweite Ableitung und zeichnet alle drei
        als Graphen in ein Koordinatensystem.
        """
        koeffizienten = self.lese_koeffizienten()
        if koeffizienten is None:
            return

        # x-Bereich einlesen
        try:
            x_min = float(self.x_min_variable.get())
            x_max = float(self.x_max_variable.get())
        except ValueError:
            messagebox.showerror("Fehler", "Bitte geben Sie gültige Zahlen für x-Min und x-Max ein.")
            return

        if x_max <= x_min:
            messagebox.showerror("Fehler", "x-Max muss größer als x-Min sein.")
            return

        # x-Werte erzeugen
        x_werte = np.linspace(x_min, x_max, 400)

        # f(x) mit np.polyval berechnen
        funktionswerte = np.polyval(koeffizienten, x_werte)

        # 1. Ableitung: neue Koeffizienten mit np.polyder
        koeffizienten_1_ableitung = np.polyder(koeffizienten)
        funktionswerte_1_ableitung = np.polyval(koeffizienten_1_ableitung, x_werte)

        # 2. Ableitung: nochmals ableiten
        koeffizienten_2_ableitung = np.polyder(koeffizienten_1_ableitung)
        funktionswerte_2_ableitung = np.polyval(koeffizienten_2_ableitung, x_werte)

        # Achse leeren und neu zeichnen
        self.koordinaten_achse.clear()

        # Originalfunktion
        self.koordinaten_achse.plot(x_werte, funktionswerte, label="f(x)")
        # Erste Ableitung
        self.koordinaten_achse.plot(x_werte, funktionswerte_1_ableitung, linestyle="--", label="f'(x)")
        # Zweite Ableitung
        self.koordinaten_achse.plot(x_werte, funktionswerte_2_ableitung, linestyle=":", label="f''(x)")

        self.koordinaten_achse.set_title("Polynom und Ableitungen")
        self.koordinaten_achse.set_xlabel("x")
        self.koordinaten_achse.set_ylabel("Funktionswerte")
        self.koordinaten_achse.grid(True)
        self.koordinaten_achse.legend()

        # Grafik aktualisieren
        self.leinwand.draw()


if __name__ == "__main__":
    hauptfenster = tk.Tk()
    oberflaeche = PolynomOberflaeche(hauptfenster)
    hauptfenster.mainloop()