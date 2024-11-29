
# Graustufenbild durch Programmanweisungen erzeugen
import numpy as np
from skimage import io

a = np.zeros((12, 18))
a[4:10, 6:14] = 1
print(a)
a= (a*255).astype(np.uint8)
io.imshow(a)
io.imsave("Rechteck_grau.jpg", a)
io.show()
