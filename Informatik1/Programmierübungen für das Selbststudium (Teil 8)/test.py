from math import *
# Das erste Programm
# Umrechnung von Grad Celsius in Grad Fahrenheit

print("Umrechnung der Temperaturen von Celsius in Fahrenheit")
anweisung="Bitte Temperatur erfassen"


celsius = input(anweisung) # input erfasst Zeichenketten
celsius = float(celsius) #float wandelt input-wert in eine Gleitkommazahl um
fahrenheit= 9/5 * celsius +32 #Berechnung erfolgt

print("Eingegebener Wert für Celsius", celsius)
print("Temperatur in Fahrenheit:" ,fahrenheit)


