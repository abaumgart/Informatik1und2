
# Bild einlesen, skalieren und in
# ein Graustufenbild umwandeln

import numpy as np
from skimage import io, color, transform

bild = io.imread("muenzen.jpg")
print(np.shape(bild))
bild_grau = color.rgb2gray(bild)
bild_grau = (bild_grau*255).astype(np.uint8)
print(np.shape(bild_grau))
bild_skaliert_grau = transform.rescale(bild_grau,0.2)
print(np.shape(bild_skaliert_grau))
io.imsave('muenzen_skaliert_grau.png',bild_grau)
io.imshow(bild_grau)
io.show()
