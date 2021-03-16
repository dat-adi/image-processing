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

# displaying the RGB original image
cv2.imshow("RGB", image)

# splitting all the colors and displaying them in the RGB color space
for (name, chan) in zip(("B", "G", "R"), cv2.split(image)):
    cv2.imshow(name, chan)

# destroying all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# displaying the image in the HSV colorspace
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

# splitting all the colors and displaying them in the HSV format
for (name, chan) in zip(("H", "S", "V"), cv2.split(hsv)):
    cv2.imshow(name, chan)

# destroying all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# displaying the image in LAB colorspace
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b*", lab)

# splitting and displaying the image in LAB colorspace
for (name, chan) in zip(("L*", "a*", "b*"), cv2.split(lab)):
    cv2.imshow(name, chan)

# destroying all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# conversion of the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# original and grayscale display
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
