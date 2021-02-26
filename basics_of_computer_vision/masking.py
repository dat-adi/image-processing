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
cv2.imshow("Original", image)

# creating a mask of that has the same dimensions of the image
# where each pixel is valued at 0
mask = np.zeros(image.shape[:2], dtype="uint8")

# creating a rectangle on the mask
# where the pixels are valued at 255
cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)
cv2.imshow("Mask", mask)

# performing a bitwise_and with the image and the mask
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask applied to Image", masked)
cv2.waitKey(0)

# creating a mask of that has the same dimensions of the image
# where each pixel is valued at 0
mask = np.zeros(image.shape[:2], dtype="uint8")

# creating a rectangle on the mask
# where the pixels are valued at 255
cv2.circle(mask, (145, 200), 100, 255, -1)
cv2.imshow("Mask", mask)

# performing a bitwise_and with the image and the mask
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask applied to Image", masked)
cv2.waitKey(0)
