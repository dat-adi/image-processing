# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 21:41:25 2019

@author: narui
"""

import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
print("width : ", image.shape[1])
print("height : ", image.shape[0])
print("channels : ", image.shape[2])

cv2.imshow("Image", image)
cv2.waitKey(0)

cv2.imwrite("newimage.jpg", image)
