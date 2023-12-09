import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
I = cv2.imread(
    "E:\\Study\\Academic\\Year - 4 Term - 2\\CSTE 4201 - Digital Image Processing\\lab-programs\\image\\onion.png"
)

# Display the original image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
plt.title("Original Image")

# Convert datatype to Double
r = I.astype(float)

# Set the gamma value
G = 0.6

# Applying the Power Law Transformation
C = 1  # You might need to adjust this constant
S = C * np.power(r, G)
T = 255 / (C * np.power(255, G))

# Converting the datatype back to integer for displaying
O = np.clip(T * S, 0, 255).astype(np.uint8)

# Display the power law transformed image
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(O, cv2.COLOR_BGR2RGB))
plt.title("Power Law Transformation")

plt.tight_layout()
plt.show()
