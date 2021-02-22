# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 21:41:25 2019

@author: narui
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

# printing out the various dimensions of the image
print("width : ", image.shape[1])
print("height : ", image.shape[0])
print("channels : ", image.shape[2])

# Displays the image using cv2.imshow
cv2.imshow("Image", image)

# Displays the image until the user presses a key closing the display
cv2.waitKey(0)

# Writing the image into the same folder as the script
# But under a new name
cv2.imwrite("newimage.jpg", image)
