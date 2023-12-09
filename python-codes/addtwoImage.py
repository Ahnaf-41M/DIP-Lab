import cv2
import matplotlib.pyplot as plt

# Read Image1
imgPath = "E:\\Study\\Academic\\Year - 4 Term - 2\\CSTE 4201 - Digital Image Processing\\lab-programs\\image\\"

# Read image1
rice = cv2.imread(imgPath + "rice.png", 1)
rice = cv2.resize(rice, (500, 500))

# Read image2
trees = cv2.imread(imgPath + "trees.tif", 1)
trees = cv2.resize(trees, (500, 500))

# Add the images
img = cv2.add(rice, trees)

# plt.imshow(rice)
plt.subplot(1, 3, 1)
plt.imshow(rice)
plt.title("Rice Image")

# plt.imshow(trees)
plt.subplot(1, 3, 2)
plt.imshow(trees)
plt.title("Tree Image")

# plt.imshow(img)
plt.subplot(1, 3, 3)
plt.imshow(img)
plt.title("Added Image")

plt.show()
