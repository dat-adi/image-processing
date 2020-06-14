import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image file")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale", gray)
cv2.waitKey(0)

(cnts, _) = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
clone = image.copy()
cv2.drawContours(clone, cnts, -1, (0, 255, 0), 2)
print("Found {} contours".format(len(cnts)))
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imshow("image", image)

(T, threshInv) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow("Threshold", threshInv)
print("Otsu's threshold value : {}".format(T))

otsu_output = cv2.bitwise_and(gray, gray, mask=threshInv)
cv2.imshow("Output", otsu_output)
cv2.waitKey(0)
