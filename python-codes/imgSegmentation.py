import cv2
import matplotlib.pyplot as plt

# Read the image
Path = "E:\\Study\\Academic\\Year - 4 Term - 2\\CSTE 4201 - Digital Image Processing\\lab-programs\\image\\peppers.png"
I = cv2.imread(Path, 1)

# Get image dimensions
height, width, planes = I.shape

# Reshape the image into a format suitable for visualization
rgb = I.reshape(height, width * planes)

# Display the reshaped image using Matplotlib
plt.imshow(rgb)
plt.axis("off")  # Hide axis
plt.show()
