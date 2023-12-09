import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read the image
Path = "E:\\Study\\Academic\\Year - 4 Term - 2\\CSTE 4201 - Digital Image Processing\\lab-programs\\image\\onion.png"
I = cv2.imread(Path, 1)

# Convert image to grayscale
I_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# Display histograms using Matplotlib
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.hist(I_gray.ravel(), bins=256, range=[0, 256])
plt.title("Histogram - 256 bins")

plt.subplot(1, 3, 2)
plt.hist(I_gray.ravel(), bins=128, range=[0, 256])
plt.title("Histogram - 128 bins")

plt.subplot(1, 3, 3)
plt.hist(I_gray.ravel(), bins=32, range=[0, 256])
plt.title("Histogram - 32 bins")

plt.tight_layout()
plt.show()
