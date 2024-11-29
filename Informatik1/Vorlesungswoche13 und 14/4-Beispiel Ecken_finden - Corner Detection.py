
# Ecken in einer Grafik finden
# Corner Detection

from skimage.feature import corner_peaks, corner_harris
import matplotlib.pyplot as plt
import numpy as np
from skimage import io, color

bild = io.imread("Kreuz.jpg")
skizze = color.rgb2gray(bild)
koord = corner_peaks(corner_harris(skizze), min_distance=10)
print(np.shape(koord))

gesamt = plt.figure()
links = gesamt.add_subplot(1,2,1)
links.set_title("Original")
links.imshow(bild)
rechts = gesamt.add_subplot(1,2,2)
rechts.set_title("Mit Eckpunkten")
for i in koord:
    x = i[1]; y = i[0]
    rechts.plot(x,y, 'ro')
rechts.imshow(bild)
gesamt.show()
