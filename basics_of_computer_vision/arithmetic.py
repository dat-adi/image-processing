# importing numpy to work with pixels
import numpy as np

# importing argument parsers
import argparse

# importing the OpenCV module
import cv2


# initializing an argument parser object
ap = argparse.ArgumentParser()

# adding the argument, providing the user an option
# to input the path of the image
ap.add_argument("-i", "--image", required=True, help="Path to the image")

# parsing the argument
args = vars(ap.parse_args())

# reading the image location through args
# and reading the image using cv2.imread
image = cv2.imread(args["image"])

# printing out details of image min, max and the wrap around
print("max of 255 :", str(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 0 :", str(cv2.subtract(np.uint8([50]), np.uint8([100]))))

print("wrap around :", str(np.uint8([200]) + np.uint8([100])))
print("wrap around :", str(np.uint8([50]) - np.uint8([100])))

# adding pixels of value 255 (white) to the image
M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)
cv2.waitKey(0)

# adding pixels of value 0 (black) to the image
M = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)
