# importing the numpy module to work with pixels in images
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


# defining a function for translation
def translate(image, x, y):
    # defining the translation matrix
    M = np.float32([[1, 0, x], [0, 1, y]])

    # the cv2.warpAffine method does the actual translation
    # containing the input image and the translation matrix
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    # we then return the image
    return shifted


# reads the image from image location
image = cv2.imread(args["image"])
cv2.imshow("Original", image)


# call the translation function to translate the image
shifted = translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)
