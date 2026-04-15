import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Symbolische Variable anlegen
x = sp.symbols('x')

# Funktion mit SymPy definieren
funktion = x**5-3*x**4+2*x**3-x+1

# Ableitung berechnen
ableitung = sp.diff(funktion, x)

print("Funktion:", funktion)
print("Ableitung:", ableitung)

f=sp.lambdify(x, funktion, "numpy")

# Werte mit NumPy erzeugen
x_werte = np.linspace(-5, 5, 100)
y_werte = f(x_werte)

# Grafik mit Matplotlib zeichnen
plt.plot(x_werte, y_werte)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Grafik der Funktion x²")
plt.grid(True)
plt.show()