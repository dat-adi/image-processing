# importing the numpy module to work with pixels in images
import numpy as np

# importing argument parsers
import argparse

# the imutils package is used for a variety of transformations
import imutils

# importing the OpenCV module
import cv2

# initializing an argument parser object
ap = argparse.ArgumentParser()

# adding the argument, providing the user an option
# to input the path of the image
ap.add_argument("-i", "--image", required=True, help="Path to the image")

# parsing the argument
args = vars(ap.parse_args())


def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted


image = cv2.imread(args["image"])
cv2.imshow("Original", image)


M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)
