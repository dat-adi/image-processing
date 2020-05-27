import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image is supposed to be given")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]

cv2.imshow("Original", image)
cv2.imshow("Thresh", thresh)

(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
hullImage = np.zeros(gray.shape[:2], dtype="uint8")

for(i, c) in enumerate(cnts):
    area = cv2.contourArea(c)
    (x, y, w, h) = cv2.boundingRect(c)
    aspectRatio = w/float(h)

    extent = area/float(w*h)

    hull = cv2.convexHull(c)
    hullArea = cv2.contourArea(hull)
    solidity = area/float(hullArea)

    cv2.drawContours(hullImage, [hull], -1, 255, -1)
    cv2.drawContours(image, [c], -1, (240, 0, 159), 3)
    shape = ""

    if 0.98 <= aspectRatio <= 1.02:
        shape = "SQUARE"
    elif aspectRatio >= 3.0:
        shape = "RECTANGLE"
    elif extent < 0.65:
        shape = "L-Piece"
    elif solidity > 0.80:
        shape = "Z-Piece"

    cv2.putText(image, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (240, 0, 159), 2)
    print("Contour {} -- aspect ratio = {}, extent = {}, solidity = {}".format(i+1, aspectRatio, extent, solidity))

cv2.imshow("Convex Hull", hullImage)
cv2.imshow("Image", image)
cv2.waitKey(0)
