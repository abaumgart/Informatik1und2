import numpy as np

A=np.matrix([[1,2],
             [3,4]
            ])
B=np.matrix([[5,6],
             [7,8]
            ])

C=A*B
print(C)

y=np.poly1d([-10,0,0,0,-1,0,1,-8])

y1=y.deriv(1)
print (y1)




