n = int(input("Bitte eine ganze Zahl n eingeben: "))
fakultaet = 1								#1
for i in range(1,n+1):
      fakultaet = fakultaet * i
print("Die Fakultaet von %d ist %d" % (n, fakultaet))
