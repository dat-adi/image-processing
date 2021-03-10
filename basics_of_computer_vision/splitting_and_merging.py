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

# splitting the image into three colors
(B, G, R) = cv2.split(image)

# displaying the colors of the image
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

# merging the colors and displaying the merged image
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)

# deleting all the windows
cv2.destroyAllWindows()

# creation of a blank image
zeroes = np.zeros(image.shape[:2], dtype="uint8")

# displaying only the red portion of the image
cv2.imshow("Red", cv2.merge([zeroes, zeroes, R]))

# displaying only the green portion of the image
cv2.imshow("Green", cv2.merge([zeroes, G, zeroes]))

# displaying only the blue portion of the image
cv2.imshow("Blue", cv2.merge([B, zeroes, zeroes]))

# waiting for a key before exiting
cv2.waitKey(0)
