# importing argument parsers
import argparse

# importing the OpenCV module
import cv2


# defining a function for rotation
def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w / 2, h / 2)

    # the cv2.getRotationMatrix2D allows us to create a
    # Rotation matrix
    M = cv2.getRotationMatrix2D(center, angle, scale)

    # the warpAffine function allows us to rotate the image
    # using the rotation matrix
    rotated = cv2.warpAffine(image, M, (w, h))

    return rotated


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

# rotating the image by 45 degrees
rotated = rotate(image, 45)
cv2.imshow("Rotated by 45 Degrees", rotated)

# rotating the image by 90 degrees
rotated = rotate(image, 90)
cv2.imshow("Rotated by -90 Degrees", rotated)

# rotating the image by 180 degrees
rotated = rotate(image, 180)
cv2.imshow("Rotated by 180 degrees", rotated)

# working with offsets in images
# then, rotating 45 degrees
(h, w) = image.shape[:2]
(cX, cY) = (w / 2, h / 2)

M = cv2.getRotationMatrix2D((cX - 50, cY - 50), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by Offset & 45 Degrees", rotated)

# used to wait for user input before closing the images
cv2.waitKey(0)
