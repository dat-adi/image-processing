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

# defining the kernel sizes for the blur operations
kernelSizes = [(3, 3), (9, 9), (15, 15)]

# displaying the different levels of average blurring with the kernels
for (kX, kY) in kernelSizes:
    blurred = cv2.blur(image, (kX, kY))
    cv2.imshow("Average ({},{})".format(kX, kY), blurred)
    cv2.waitKey(0)

# destroying all windows
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# displaying the different levels of gaussian blurring with the kernels
for (kX, kY) in kernelSizes:
    blurred = cv2.GaussianBlur(image, (kX, kY), 0)
    cv2.imshow("Gaussian ({},{})".format(kX, kY), blurred)
    cv2.waitKey(0)

# destroying all windows
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# displaying the different levels of median blurring with the kernels
for k in (3, 9, 15):
    blurred = cv2.medianBlur(image, k)
    cv2.imshow("Median {}".format(k), blurred)
    cv2.waitKey(0)
