import numpy as np

# --- Polynom-Koeffizienten (f(x) = x^3 - 6x^2 + 9x + 15) ---
f = np.array([1, -6, 9, 15])

print("Koeffizienten des Polynoms:")
print(f)

# --- 1. Funktionswert berechnen ---
x0 = 2
y0 = np.polyval(f, x0)
print(f"\nf({x0}) = {y0}")

# --- 2. Nullstellen ---
nullstellen = np.roots(f)
nullstellen_real = nullstellen[np.isreal(nullstellen)].real
print("\nReelle Nullstellen:")
print(nullstellen_real)

# --- 3. Erste Ableitung f'(x) ---
f1 = np.polyder(f)
print("\nKoeffizienten von f'(x):")
print(f1)

# --- 4. Extremstellen: f'(x) = 0 ---
extrema = np.roots(f1)
extrema_real = extrema[np.isreal(extrema)].real
print("\nKandidaten für Extremstellen (f'(x)=0):")
print(extrema_real)

# Funktionswerte an diesen Stellen
for x_ext in extrema_real:
    y_ext = np.polyval(f, x_ext)
    print(f"f({x_ext}) = {y_ext}")

# --- 5. Zweite Ableitung f''(x) ---
f2 = np.polyder(f1)
print("\nKoeffizienten von f''(x):")
print(f2)

# --- 6. Wendepunkte: f''(x) = 0 ---
wendepunkte = np.roots(f2)
wendepunkte_real = wendepunkte[np.isreal(wendepunkte)].real
print("\nKandidat für Wendepunkt (f''(x)=0):")
print(wendepunkte_real)

# Funktionswert am Wendepunkt
for x_w in wendepunkte_real:
    y_w = np.polyval(f, x_w)
    print(f"f({x_w}) = {y_w}")