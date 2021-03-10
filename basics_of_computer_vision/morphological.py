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

# displaying the original image
cv2.imshow("Original", image)

# utilization of erosion threefold times
for i in range(0, 3):
    eroded = cv2.erode(gray.copy(), None, iterations=i + 1)
    cv2.imshow("Eroded {} times".format(i + 1), eroded)
    cv2.waitKey(0)

# destruction of all the windows
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# utilization of dilation threefold times
for i in range(0, 3):
    dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)
    cv2.imshow("Dilated {} times".format(i + 1), dilated)
    cv2.waitKey(0)

# destruction of all the windows
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# creation of three different kernels to use in morphology
kernelSizes = [(3, 3), (5, 5), (7, 7)]

# utilization of the morphological Opening operation
for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening: ({}, {})".format(kernelSize[0], kernelSize[1]), opening)
    cv2.waitKey(0)

# destruction of all the windows
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# utilization of the morphological closing operation
for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing: ({}, {})".format(kernelSize[0], kernelSize[1]), closing)
    cv2.waitKey(0)

# destruction of all the windows
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# utilization of the morphological gradient operation
for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("Gradient: ({}, {})".format(kernelSize[0], kernelSize[1]), gradient)
    cv2.waitKey(0)
