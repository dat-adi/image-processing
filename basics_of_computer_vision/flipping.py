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

# reading the image from the image location
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# flipping the image horizontally
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

# flipping the image vertically
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

# flipping the image vertically and horizontally
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Vertically and Horizontally", flipped)

# wait for the user's key to proceed
cv2.waitKey(0)
