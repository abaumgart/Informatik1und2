import numpy as np

print("Polynom-Erfassung und Kurvendiskussion")

# ------------------------------------------
# Schritt 1: Grad des Polynoms erfassen
# ------------------------------------------
grad = int(input("Bitte geben Sie den Grad des Polynoms ein: "))

print(f"Ein Polynom {grad}. Grades hat {grad + 1} Koeffizienten.")

# ------------------------------------------
# Schritt 2: Koeffizienten erfassen
# (von a_n bis a_0)
# ------------------------------------------
koeffizienten = []

for exponent in range(grad, -1, -1):
    wert = float(input(f"Koeffizient für x^{exponent}: "))
    koeffizienten.append(wert)

print("\nEingegebene Koeffizienten (von a_n bis a_0):")
print(koeffizienten)

# Python-Liste -> NumPy-Array
f = np.array(koeffizienten)
print("\nKoeffizienten als NumPy-Array:")
print(f)

# ------------------------------------------
# Schritt 3: Funktionswert für einen x-Wert
# ------------------------------------------
x0 = float(input("\nBitte geben Sie einen x-Wert zur Berechnung von f(x) ein: "))
y0 = np.polyval(f, x0)

print(f"f({x0}) = {y0}")

# ------------------------------------------
# Schritt 4: Nullstellen berechnen
# ------------------------------------------
nullstellen = np.roots(f)
nullstellen_real = nullstellen[np.isreal(nullstellen)].real

print("\nReelle Nullstellen:")
print(nullstellen_real)

# ------------------------------------------
# Schritt 5: Erste Ableitung (f') und Extremstellen
# ------------------------------------------
f1 = np.polyder(f)
print("\nKoeffizienten der 1. Ableitung f'(x):")
print(f1)

extrema = np.roots(f1)
extrema_real = extrema[np.isreal(extrema)].real

print("\nKandidaten für Extremstellen (f'(x)=0):")
print(extrema_real)

for x_ext in extrema_real:
    y_ext = np.polyval(f, x_ext)
    print(f"f({x_ext}) = {y_ext}")

# ------------------------------------------
# Schritt 6: Zweite Ableitung (f'') und Wendepunkt
# ------------------------------------------
f2 = np.polyder(f1)
print("\nKoeffizienten der 2. Ableitung f''(x):")
print(f2)

# NumPy liefert hier **nur** die Nullstellen von f''(x),
# also Stellen, an denen die zweite Ableitung = 0 ist.
# Das sind *Kandidaten* für Wendepunkte.
#
# Kurzfassung für Studierende:
# Ein Wendepunkt liegt nur dann vor,
# wenn sich an dieser Stelle die Krümmung ändert.
# f''(x) = 0 ist also eine notwendige,
# aber keine hinreichende Bedingung.
# NumPy kann den Krümmungswechsel nicht prüfen,
# deshalb spricht man hier von "Kandidaten".

wendepunkte = np.roots(f2)
wendepunkte_real = wendepunkte[np.isreal(wendepunkte)].real

print("\nKandidat für Wendepunkt (f''(x)=0):")
print(wendepunkte_real)

for x_w in wendepunkte_real:
    y_w = np.polyval(f, x_w)
    print(f"f({x_w}) = {y_w}")