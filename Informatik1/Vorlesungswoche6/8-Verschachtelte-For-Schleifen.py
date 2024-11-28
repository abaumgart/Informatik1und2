for i in range(3,33,3):
      print(i,end=" ")
print()
print()
for i in range(1,11,1):					#1
      for j in range(i,i*10+i,i):					#2
            print("%6d"%j,end=" ")					#3
      print()                           #4
print()
print()
for i in range(1,11,1):
      for j in range(1,11,1):
            print("%6d"%(j*i),end=" ")
      print()


