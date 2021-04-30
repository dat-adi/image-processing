# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 19:32:17 2019

@author: Dat Adithya
"""

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

# assigns the image dimensions to two different variables
(h, w) = image.shape[:2]

# Displays the image using cv2.imshow
cv2.imshow("Original", image)

# Displays the image until the user presses a key closing the display
cv2.waitKey(0)

# Values of the pixel before assigning a color to it
(b, g, r) = image[0, 0]
print("Pixel at (0,0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

# Values of the pixel after assigning a color to it
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0,0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

# Displaying the altered image
cv2.imshow("Original-RedDot@0,0", image)
cv2.waitKey(0)

# Providing values to display a quarter of the image
(cX, cY) = (w / 2, h / 2)

# Displaying a quarter of the image
tl = image[0 : int(cY), 0 : int(cX)]
cv2.imshow("Top Left Corner", tl)
cv2.waitKey(0)

# Top Right, Bottom Right, Bottom Left
tr = image[0 : int(cY), int(cX) : w]
br = image[int(cY) : h, int(cX) : w]
bl = image[int(cY) : h, 0 : int(cX)]

print("Top Right Corner", tr)
print("Bottom Right Corner", br)
print("Bottom Left Corner", bl)

# Altering the first quarter of the image to turn into green color
image[0 : int(cY), 0 : int(cX)] = (0, 255, 0)

# Displaying the updated image
cv2.imshow("Updated", image)
cv2.waitKey(0)
