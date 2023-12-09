import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
Path = "E:\\Study\\Academic\\Year - 4 Term - 2\\CSTE 4201 - Digital Image Processing\\lab-programs\\image\\bitplane.bmp"
I = cv2.imread(Path, 0)

# Make a copy of the original image
G = np.copy(I)

# Get image dimensions
rows, cols = I.shape

# Get user input for thresholds and slopes
T1 = int(input("Enter value of t1(Threshold 1): "))
T2 = int(input("Enter value of t2(Threshold 2): "))
s1 = float(input("Enter value of slope 1: "))
s2 = float(input("Enter value of slope 2: "))
s3 = float(input("Enter value of slope 3: "))

# Calculate coefficients
coeffT1 = s1 * T1
coeffT2 = s2 * (T2 - T1) + coeffT1

# Apply contrast stretching
for i in range(rows):
    for j in range(cols):
        if I[i, j] < T1:
            G[i, j] = np.floor(s1 * I[i, j])
        elif T1 <= I[i, j] < T2:
            G[i, j] = np.floor(s2 * (I[i, j] - T1) + coeffT1)
        else:
            G[i, j] = np.floor(s3 * (I[i, j] - T2) + coeffT2)

# Display the images and histograms
cv2.imshow("Original image", I)
cv2.imshow("Result of Contrast Stretching", G)
cv2.waitKey(0)

# Calculate histograms
hist_I = cv2.calcHist([I], [0], None, [256], [0, 256])
hist_G = cv2.calcHist([G], [0], None, [256], [0, 256])

# Plot histograms

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(hist_I)
plt.title("Histogram for original Image")

plt.subplot(2, 1, 2)
plt.plot(hist_G)
text1 = f"Histogram for Contrast Stretching with T1={T1}, T2={T2}, s1={s1}, s2={s2}, s3={s3}"
plt.title(text1)

plt.show()
