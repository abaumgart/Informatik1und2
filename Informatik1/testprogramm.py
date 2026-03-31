import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Symbolische Variable anlegen
x = sp.symbols('x')

# Funktion mit SymPy definieren
funktion = x**2

# Ableitung berechnen
ableitung = sp.diff(funktion, x)

print("Funktion:", funktion)
print("Ableitung:", ableitung)

# Werte mit NumPy erzeugen
x_werte = np.linspace(-5, 5, 100)
y_werte = x_werte**2

# Grafik mit Matplotlib zeichnen
plt.plot(x_werte, y_werte)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Grafik der Funktion x²")
plt.grid(True)
plt.show()