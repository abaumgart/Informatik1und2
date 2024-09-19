
import math

# Quadratwurzel
x = 16
print("Quadratwurzel:", math.sqrt(x))  # Ergebnis: 4.0

# Potenz
print("Potenz:", math.pow(2, 3))  # Ergebnis: 8.0

# Sinus
print("Sinus:", math.sin(math.pi / 2))  # Ergebnis: 1.0

# Cosinus
print("Cosinus:", math.cos(math.pi))  # Ergebnis: -1.0

# Logarithmus
print("Natürlicher Logarithmus:", math.log(10))  # Ergebnis: 2.302585092994046
print("Logarithmus zur Basis 10:", math.log10(10))  # Ergebnis: 1.0


a = 2
b = 3
c = 4

result = a ** 2 + b * c - math.sqrt(a * b * c)
print("Ergebnis des komplexen Ausdrucks:", result)