class Handy:
    def __init__(self, akku, speicher):
        self.akku = akku
        self.speicher = speicher

    # Akkustand anzeigen
    def akku_pruefen(self):
        print(f"Aktueller Akkustand: {self.akku}%")

    # Prüfen ob genug Akku für eine Funktion da ist
    def funktionspruefer(self, benoetigter_akku):
        if self.akku >= benoetigter_akku:
            return True
        else:
            print("Nicht genug Akku für diese Funktion.")
            return False

    # Telefonieren
    def telefonieren(self, minuten):
        verbrauch = minuten * 2
        if self.funktionspruefer(verbrauch):
            self.akku -= verbrauch
            print(f"Du hast {minuten} Minuten telefoniert.")
            self.akku_pruefen()

    # SMS senden
    def sms_senden(self, nummer, nachricht):
        if self.funktionspruefer(1):
            self.akku -= 1
            print(f"SMS an {nummer}: {nachricht}")
            self.akku_pruefen()


# Beispiel
mein_handy = Handy(100, 128)
mein_altes_handy = Handy(25, 64)

mein_handy.akku_pruefen()
mein_altes_handy.akku_pruefen()
mein_handy.telefonieren(5)
mein_handy.sms_senden("017612345678", "Hallo!")