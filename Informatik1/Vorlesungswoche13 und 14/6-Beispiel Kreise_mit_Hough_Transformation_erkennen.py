
# Kreise mit der Hough-Transformation ermitteln

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from skimage import io, color
from skimage.transform import hough_circle, hough_circle_peaks
from skimage.feature import canny

bild = io.imread("muenzen_skaliert.png")
bild_grau = color.rgb2gray(bild)
kanten = canny(bild_grau)
hough_radien = np.arange(25, 70, 4)
ergebnis = hough_circle(kanten, hough_radien)
ka, kx, ky, kr = hough_circle_peaks(ergebnis,
                                hough_radien,
                                    total_num_peaks=18)

gesamt = plt.figure()
ausgabe = gesamt.add_subplot(1,1,1)
ausgabe.set_title("Münzen mit Hough-Kreisen")
ausgabe.imshow(bild)
for x,y,radius in zip(kx,ky,kr):
    kreis = patches.Circle((x,y),radius,linewidth=2,
                           edgecolor='r',facecolor='none')
    ausgabe.add_patch(kreis)
gesamt.show()
