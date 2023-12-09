import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
Path = "E:\\Study\\Academic\\Year - 4 Term - 2\\CSTE 4201 - Digital Image Processing\\lab-programs\\image\\pollen.tif"
I = cv2.imread(Path, 0)

num_of_pixels = I.shape[0] * I.shape[1]

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(I, cmap="gray")
plt.title("Original Image")
plt.axis("off")

HIm = np.zeros_like(I)
freq = np.zeros(256)
probf = np.zeros(256)
probc = np.zeros(256)
cum = np.zeros(256)
output = np.zeros(256)

# Calculate histogram and probabilities
for i in range(I.shape[0]):
    for j in range(I.shape[1]):
        value = I[i, j]
        freq[value] += 1
        probf[value] = freq[value] / num_of_pixels

# Calculate cumulative distribution probability
sum = 0
no_bins = 255
for i in range(256):
    sum += freq[i]
    cum[i] = sum
    probc[i] = cum[i] / num_of_pixels
    output[i] = round(probc[i] * no_bins)

# Perform histogram equalization
for i in range(I.shape[0]):
    for j in range(I.shape[1]):
        HIm[i, j] = output[I[i, j]]

# Display histogram equalized image
plt.subplot(2, 2, 2)
plt.imshow(HIm, cmap="gray")
plt.title("Histogram Equalization")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.hist(I.ravel(), 256, [0, 256])
plt.title("Histogram of Original Image")

plt.subplot(2, 2, 4)
plt.hist(HIm.ravel(), 256, [0, 256])
plt.title("Histogram of Image after equalization")

plt.tight_layout()
plt.show()
