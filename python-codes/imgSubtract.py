import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read the image
I = cv2.imread(
    "E:\\Study\\Academic\\Year - 4 Term - 2\\CSTE 4201 - Digital Image Processing\\lab-programs\\image\\rice.png"
)

# Display the original image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
plt.title("Original Image")

# Subtract a constant value (50 in this case)
constant_value = 50
imgSubConstant = np.clip(I.astype(int) - constant_value, 0, 255).astype(np.uint8)

# Display the subtracted image with a constant value
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(imgSubConstant, cv2.COLOR_BGR2RGB))
plt.title(f"Subtracted Image (Constant {constant_value})")

plt.tight_layout()
plt.show()
