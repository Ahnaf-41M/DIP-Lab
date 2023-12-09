import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
Path = "E:\\Study\\Academic\\Year - 4 Term - 2\\CSTE 4201 - Digital Image Processing\\lab-programs\\image\\pattern_blur.tif"
I = cv2.imread(Path, 1)

# Define the filter kernel (3x3 averaging filter)
h = np.ones((3, 3), dtype=np.float32) / 9

# Apply the filter using OpenCV's filter2D function
I2 = cv2.filter2D(I, -1, h)

# Display the original image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
plt.title("Original Image")

# Display the filtered image
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(I2, cv2.COLOR_BGR2RGB))
plt.title("Filtered Image")

plt.tight_layout()
plt.show()
