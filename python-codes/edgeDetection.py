import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read the image
Path = "E:\\Study\\Academic\\Year - 4 Term - 2\\CSTE 4201 - Digital Image Processing\\lab-programs\\image\\saturn.png"
I = cv2.imread(Path, 1)

# Convert to grayscale
I_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# Apply edge detection using Sobel, Prewitt, and Roberts operators
sEdge = cv2.Sobel(I_gray, cv2.CV_64F, 1, 1, ksize=3)
prEdge = cv2.filter2D(
    I_gray,
    -1,
    cv2.getDerivKernels(1, 1, 3, True)[0] * cv2.getDerivKernels(1, 1, 3, True)[1].T,
)
roEdge = cv2.filter2D(
    I_gray,
    -1,
    cv2.getDerivKernels(1, 0, 3, True)[0] * cv2.getDerivKernels(1, 0, 3, True)[1].T
    + cv2.getDerivKernels(0, 1, 3, True)[0] * cv2.getDerivKernels(0, 1, 3, True)[1].T,
)

# Display images
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(np.absolute(sEdge), cmap="gray")
plt.title("Sobel")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(np.absolute(prEdge), cmap="gray")
plt.title("Prewitt")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(np.absolute(roEdge), cmap="gray")
plt.title("Roberts")
plt.axis("off")

plt.tight_layout()
plt.show()
