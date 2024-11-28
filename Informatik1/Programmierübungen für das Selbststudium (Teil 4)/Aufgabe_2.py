
faktor = 0.73549875
print("PS | kW")
print()
for ps in range(50,205,5):
      kW = ps*faktor
      print("%9.2f %9.2f" % (ps, kW))
