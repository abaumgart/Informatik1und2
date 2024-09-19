
import math
import matplotlib.pyplot as plt

def main():
    # 1. Deklaration und Initialisierung der Variablen
    x = 5
    y = 3
    z = 2

    # 2. Berechnung des ersten Ausdrucks
    result_1 = (x + y) * z / x
    print("Ergebnis des ersten Ausdrucks:", result_1)

    # 3. Berechnung des zweiten Ausdrucks
    result_2 = x ** 2 + y ** 2 - math.sqrt(z)
    print("Ergebnis des zweiten Ausdrucks:", result_2)

    # 4. Berechnung des dritten Ausdrucks
    result_3 = math.log10(x * y * z)
    print("Ergebnis des dritten Ausdrucks:", result_3)

    # 5. Erstellen von Datenpunkten für den Graphen
    xs = range(1, 101)
    ys_1 = [(xi + y) * z / xi for xi in xs]
    ys_2 = [xi ** 2 + y ** 2 - math.sqrt(z) for xi in xs]
    ys_3 = [math.log10(xi * y * z) for xi in xs]

    # 6. Erstellen des Graphen
    plt.figure(figsize=(10, 5))

    # Subplot 1
    plt.subplot(1, 3, 1)
    plt.plot(xs, ys_1, label='(x + y) * z / x')
    plt.xlabel('x')
    plt.ylabel('Ergebnis')
    plt.title('Erster Ausdruck')
    plt.legend()

    # Subplot 2
    plt.subplot(1, 3, 2)
    plt.plot(xs, ys_2, label='x^2 + y^2 - sqrt(z)', color='g')
    plt.xlabel('x')
    plt.ylabel('Ergebnis')
    plt.title('Zweiter Ausdruck')
    plt.legend()

    # Subplot 3
    plt.subplot(1, 3, 3)
    plt.plot(xs, ys_3, label='log10(x * y * z)', color='r')
    plt.xlabel('x')
    plt.ylabel('Ergebnis')
    plt.title('Dritter Ausdruck')
    plt.legend()

    # Zeigen des Graphen
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()