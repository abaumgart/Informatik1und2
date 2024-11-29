
# Bild einlesen, darstellen und in
# anderen Formaten eine Kopie heraus schreiben

import numpy as np
from skimage import io

bild = io.imread("muenzen.jpg")
print("Zeilen, Spalten: ",np.shape(bild))
io.imsave("muenzen_kopie.jpg",bild)
io.imsave("muenzen_kopie.png",bild)
io.imsave("muenzen_kopie.bmp",bild)
io.imshow(bild)
io.show()
