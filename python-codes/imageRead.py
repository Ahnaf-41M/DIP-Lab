import cv2
import matplotlib.pyplot as plt

# Read the image
Path = "E:\\Study\\Academic\\Year - 4 Term - 2\\CSTE 4201 - Digital Image Processing\\lab-programs\\image\\onion.png"
I = cv2.imread(Path, 1)

# Get the dimensions of the image
r, c, _ = I.shape  # Assuming it's a color image (3 channels)

# Display the original image
plt.subplot(1, 2, 1)
plt.imshow(I)
plt.title("Original Image")

# Resize the image to a specific size (50x50)
J = cv2.resize(I, (50, 50))

# Write the resized image
cv2.imwrite("test.jpg", J)

# Display the resized image
plt.subplot(1, 2, 2)
plt.imshow(J)
plt.title("Resized Image")

plt.show()
