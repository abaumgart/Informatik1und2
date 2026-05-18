import numpy as np
a11=2
a12=5
a21=1
a22=3

b11=3
b12=5
b21=3
b22=9

matrix1=[[a11,a12],[a21,a22]]
matrix2=[[b11,b12],[b21,b22]]
ma1np=np.array(matrix1)
ma2np=np.array(matrix2)

ergebnisAddition = ma1np+ma2np
print (ergebnisAddition)
ergebnisSubtraktion=ma1np-ma2np
print(ergebnisSubtraktion)
ergebnisMultiplikation=ma1np@ma2np
print(ergebnisMultiplikation)

transponierteMatrix1= ma1np.T
print (ma1np)
print (transponierteMatrix1)

determinateMAtrix1=np.linalg.det(ma1np)
print(determinateMAtrix1)