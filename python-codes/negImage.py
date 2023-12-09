import cv2
import matplotlib.pyplot as plt

# Read the image
I = cv2.imread(
    "E:\\Study\\Academic\\Year - 4 Term - 2\\CSTE 4201 - Digital Image Processing\\lab-programs\\image\\onion.png"
)

# Display the original image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
plt.title("Original Image")

# Calculate the negative of the image
L = 2**8
neg = (L - 1) - I

# Display the negative image
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(neg, cv2.COLOR_BGR2RGB))
plt.title("Negative Image")

plt.tight_layout()
plt.show()
