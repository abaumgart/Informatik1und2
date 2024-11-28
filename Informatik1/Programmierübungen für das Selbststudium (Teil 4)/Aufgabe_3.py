
jahr = int(input("Bitte Jahreszahl eingeben: "))
if jahr%4==0:
      if jahr%100==0:
            if jahr%400==0:
                  if jahr==4000:
                        print("Kein Schaltjahr")
                  else:
                        print("Schaltjahr")
            else:
                  print("Kein Schaltjahr")
      else:
            print("Schaltjahr")
else:
      print("Kein Schaltjahr")
