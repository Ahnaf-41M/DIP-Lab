import cv2
import matplotlib.pyplot as plt

# Read the image
Path = "E:\\Study\\Academic\\Year - 4 Term - 2\\CSTE 4201 - Digital Image Processing\\lab-programs\\image\\pollen.tif"
I = cv2.imread(Path, 0)

# Display original image and its histogram
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(I, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.hist(I.ravel(), 256, [0, 256])
plt.title("Histogram of Original Image")

# Apply histogram equalization
j = cv2.equalizeHist(I)

# Display image after histogram equalization and its histogram
plt.subplot(2, 2, 2)
plt.imshow(j, cmap="gray")
plt.title("Image after histogram equalization")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.hist(j.ravel(), 256, [0, 256])
plt.title("Histogram of Image after equalization")

plt.tight_layout()
plt.show()
