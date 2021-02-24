# importing the OpenCV module
import cv2

# importing argument parsers
import argparse

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

# displaying the width and height of the image
print("Width", image.shape[1])
print("Height", image.shape[0])

# cropping the image manually
face = image[:400, :600]
cv2.imshow("Face", face)
cv2.waitKey(0)

# cropping the image manually
body = image[400:600, 120:600]
cv2.imshow("Body", body)
cv2.waitKey(0)
