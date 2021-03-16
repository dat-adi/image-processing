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

# conversion of the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# gaussian blurring the image with a (7, 7) kernel
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

# Binary threshold inverse operation
(T, threshInv) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)

# Binary threshold operation
(T, thresh) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

# providing the bitwise and output of the image and the threshold
cv2.imshow("Output", cv2.bitwise_and(image, image, mask=threshInv))
cv2.waitKey(0)
