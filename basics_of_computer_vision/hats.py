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

# conversion of the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# structuring the kernel to be used in cv2.morphologyEx()
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))

# performing a blackhat morphological operation
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)

# performing a tophat morphological operation
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)

# Displaying the three different images
cv2.imshow("Original", image)
cv2.imshow("BlackHat", blackhat)
cv2.imshow("TopHat", tophat)
cv2.waitKey(0)
