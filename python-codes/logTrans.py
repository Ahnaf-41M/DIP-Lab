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

# Constant determining the nature of the log curve
C = 1

# Performing log transformation
S = C * np.log(1 + r)
T = 255 / (C * np.log(256))

# Converting the datatype back to integer for displaying
B = np.clip(T * S, 0, 255).astype(np.uint8)

# Display the log-transformed image
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(B, cv2.COLOR_BGR2RGB))
plt.title("Log Transformation")

plt.tight_layout()
plt.show()
