print("Umrechnungsprogramm für Temperaturen")
print("------------------------------------") # Das ist die Trennlinie
print()
# Jetzt folgt die Berechnung
# ....
# celsius = 15 # 15 Grad Celsius. Wird später auf eine Tastatureingabe umgestellt
celsius = input("Bitte geben Sie die Temperatur in Celsius ein:")
celsius = float(celsius)
fahrenheit=9/5*celsius+32
print("Fahrenheit: "+str(fahrenheit))