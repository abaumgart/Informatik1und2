
# Deklarieren Sie die Sekundenzahl, die umgewandelt werden soll
sekundenbetrag = 50  

# Anzahl der Stunden berechnen und modifizieren, damit sie im Bereich 0-23 liegt
stunden = (sekundenbetrag // 3600) % 24

# Berechnung des Restwertes nach Entfernung der Stunden
rest = sekundenbetrag % 3600

# Anzahl der Minuten berechnen
minuten = rest // 60

# Anzahl der Sekunden berechnen
sekunden = rest % 60

print(f"Gesamtsekunden: {sekundenbetrag}")
print(f"h = {stunden}")
print(f"m = {minuten}")
print(f"s = {sekunden}")
print()

