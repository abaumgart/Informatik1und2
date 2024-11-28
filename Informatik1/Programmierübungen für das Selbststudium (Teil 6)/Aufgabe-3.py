
rein = open("Schraube.stl","r")
raus = open("Dreiecke.dat","w")
inhalt = rein.readlines()
rein.close()
for i in inhalt:
    if "vertex" in i:
        string,x,y,z = i.split()
        raus.write(x+" "+y+" "+z+"\n")    
raus.close()

    


    

