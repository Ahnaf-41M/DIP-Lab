import cv2
import matplotlib.pyplot as plt
import math
import numpy as np

# Read the image in greyscale
Path = "E:\\Study\\Academic\\Year - 4 Term - 2\\CSTE 4201 - Digital Image Processing\\lab-programs\\image\\bitplane.bmp"
img = cv2.imread(Path, 0)

# Iterate over each pixel and change pixel value to binary using np.binary_repr() and store it in a list.
lst = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        lst.append(np.binary_repr(img[i][j], width=8))  # width = no. of bits

# We have a list of strings where each string represents binary pixel value. To extract bit planes we need to iterate over the strings and store the characters corresponding to bit planes into lists.
# Multiply with 2^(n-1) and reshape to reconstruct the bit image.
eight_bit_img = (np.array([int(i[0]) for i in lst], dtype=np.uint8) * 128).reshape(
    img.shape[0], img.shape[1]
)
seven_bit_img = (np.array([int(i[1]) for i in lst], dtype=np.uint8) * 64).reshape(
    img.shape[0], img.shape[1]
)
six_bit_img = (np.array([int(i[2]) for i in lst], dtype=np.uint8) * 32).reshape(
    img.shape[0], img.shape[1]
)
five_bit_img = (np.array([int(i[3]) for i in lst], dtype=np.uint8) * 16).reshape(
    img.shape[0], img.shape[1]
)
four_bit_img = (np.array([int(i[4]) for i in lst], dtype=np.uint8) * 8).reshape(
    img.shape[0], img.shape[1]
)
three_bit_img = (np.array([int(i[5]) for i in lst], dtype=np.uint8) * 4).reshape(
    img.shape[0], img.shape[1]
)
two_bit_img = (np.array([int(i[6]) for i in lst], dtype=np.uint8) * 2).reshape(
    img.shape[0], img.shape[1]
)
one_bit_img = (np.array([int(i[7]) for i in lst], dtype=np.uint8) * 1).reshape(
    img.shape[0], img.shape[1]
)

plt.subplot(2, 4, 1)
plt.imshow(eight_bit_img)
plt.title("Eight Bit")

plt.subplot(2, 4, 2)
plt.imshow(seven_bit_img)
plt.title("Seven Bit")

plt.subplot(2, 4, 3)
plt.imshow(six_bit_img)
plt.title("Six Bit")

plt.subplot(2, 4, 4)
plt.imshow(five_bit_img)
plt.title("Five Bit")

plt.subplot(2, 4, 5)
plt.imshow(four_bit_img)
plt.title("Four Bit")

plt.subplot(2, 4, 6)
plt.imshow(three_bit_img)
plt.title("Three Bit")

plt.subplot(2, 4, 7)
plt.imshow(two_bit_img)
plt.title("Two Bit")

plt.subplot(2, 4, 8)
plt.imshow(one_bit_img)
plt.title("One Bit")
plt.show()


# Concatenate these images for ease of display using cv2.hconcat()
# finalr = cv2.hconcat([eight_bit_img, seven_bit_img, six_bit_img, five_bit_img])
# finalv = cv2.hconcat([four_bit_img, three_bit_img, two_bit_img, one_bit_img])

# # Vertically concatenate
# final = cv2.hconcat([finalr, finalv])
# # Display the images
# plt.imshow(eight_bit_img)
# plt.show()
