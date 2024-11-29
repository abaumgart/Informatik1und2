
# Bild einlesen und Kanten mit Canny-Filter ermitteln

import numpy as np
from skimage import io, feature

bild = io.imread("muenzen_skaliert_grau.png")
print(np.shape(bild))
kanten = feature.canny(bild)
io.imshow(kanten)
io.show()
