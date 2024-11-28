

rein = open("Ergebnisse.txt","r")
inhalt = rein.readlines()
rein.close()
X=[]; Y=[]; Z=[]; W=[]
for i in 0,1,2:
    del inhalt[0]
for i in inhalt:
    j = i.replace(",",".") 
    x,y,z,w = j.split()
    X.append(float(x))
    Y.append(float(y))
    Z.append(float(z))
    W.append(float(w))
print("X-Max-Min: ",max(X),min(X))
print("Y-Max-Min: ",max(Y),min(Y))
print("Z-Max-Min: ",max(Z),min(Z))
print("Wert-Max-Min: ",max(W),min(W))
    

