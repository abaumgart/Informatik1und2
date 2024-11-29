
# Abgleich von Vorlagen - Template-Matching

import numpy as np
import matplotlib.pyplot as plt
from skimage import data, io, color
from skimage.feature import match_template

bild = io.imread("muenzen_skaliert.png")
bild_grau = color.rgb2gray(bild)
vorlage = io.imread("vorlage.png")
vorlage_grau = color.rgb2gray(vorlage)
h, v = vorlage_grau.shape
ergebnis = match_template(bild_grau, vorlage_grau)
ij = np.unravel_index(np.argmax(ergebnis),
                      ergebnis.shape)
y,x = ij

gesamt = plt.figure() 
links = gesamt.add_subplot(1,2, 1)
links.imshow(vorlage)
links.set_axis_off()
rechts = gesamt.add_subplot(1,2,2)
rechts.imshow(bild)
rechts.set_axis_off()
markierung = plt.Rectangle((x, y), v, h,
                           edgecolor='r', facecolor='none')
rechts.add_patch(markierung)
gesamt.show()
