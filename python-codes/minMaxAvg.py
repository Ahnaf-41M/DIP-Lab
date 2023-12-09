import cv2
import numpy as np

# Read the image
I = cv2.imread(
    "E:\\Study\\Academic\\Year - 4 Term - 2\\CSTE 4201 - Digital Image Processing\\lab-programs\\image\\onion.png",
    0,
)

# Find minimum, maximum, and average intensity values using built-in functions
min_val = np.min(I)
max_val = np.max(I)
avg_val = np.mean(I)

print("Minimum Value (Using Built-in Function):", min_val)
print("Maximum Value (Using Built-in Function):", max_val)
print("Average Value (Using Built-in Function):", avg_val)

# Calculate the min, max, and average intensity values without built-in functions
min_val_custom = np.min(I.reshape(-1))  # Reshape to 1D array and find the minimum
max_val_custom = np.max(I.reshape(-1))  # Reshape to 1D array and find the maximum
avg_val_custom = np.mean(I.reshape(-1))  # Reshape to 1D array and find the mean

print("\nMinimum Value (Without Built-in Function):", min_val_custom)
print("Maximum Value (Without Built-in Function):", max_val_custom)
print("Average Value (Without Built-in Function):", avg_val_custom)
