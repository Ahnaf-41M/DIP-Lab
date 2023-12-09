import cv2
import matplotlib.pyplot as plt
import math
import numpy as np

# Read the image in greyscale
Path = "E:\\Study\\Academic\\Year - 4 Term - 2\\CSTE 4201 - Digital Image Processing\\lab-programs\\image\\kids.tif"
img = cv2.imread(Path, 0)

kernel = np.ones((15, 15), np.uint8)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
erosion = cv2.erode(closing, kernel, iterations=1)

boundaryImg = closing - erosion

cv2.imshow("original", img)
cv2.imshow("output", boundaryImg)
cv2.waitKey()
