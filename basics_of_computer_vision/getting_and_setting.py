# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 19:32:17 2019

@author: narui
"""

import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
cv2.imshow("Original", image)
cv2.waitKey(0)

(b, g, r) = image[0, 0]
print("Pixel at (0,0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0,0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))
cv2.imshow("Original-RedDot@0,0", image)
cv2.waitKey(0)

(cX, cY) = (w / 2, h / 2)

tl = image[0 : int(cY), 0 : int(cX)]
cv2.imshow("Top Left Corner", tl)
cv2.waitKey(0)

tr = image[0 : int(cY), int(cX) : w]
br = image[int(cY) : h, int(cX) : w]
bl = image[int(cY) : h, 0 : int(cX)]

print("Top Right Corner", tr)
print("Bottom Right Corner", br)
print("Bottom Left Corner", bl)

image[0:cY, 0:cX] = (0, 255, 0)

cv2.imshow("Updated", image)
cv2.waitKey(0)
