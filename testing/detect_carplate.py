import cv2
import argparse
import numpy as np


def auto_canny(image, sigma=0.33):
    v = np.median(image)
    lower = int(max(0, (1.0-sigma)*v))
    upper = int(max(255, (1.0+sigma)*v))
    edged = cv2.Canny(image, lower, upper)
    return edged


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image file")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale", gray)
cv2.waitKey(0)

blurred = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imshow("image", image)

(T, threshInv) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Threshold", threshInv)
print("Otsu's threshold value : {}".format(T))

otsu_output = cv2.bitwise_and(gray, gray, mask=threshInv)
cv2.imshow("Output", otsu_output)
cv2.waitKey(0)

tight = cv2.Canny(otsu_output, 225, 250)
auto = auto_canny(otsu_output)
cv2.imshow("Tight Canny", tight)
cv2.imshow("Auto Canny Result", auto)
cv2.waitKey(0)

(cnts, _) = cv2.findContours(auto.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
clone = gray.copy()

cv2.drawContours(clone, cnts, -1, (0, 255, 0), 2)
print("Found {} contours".format(len(cnts)))
hull = []

for i in range(len(cnts)):
    hull.append(cv2.convexHull(cnts[i], False))

for(i, c) in enumerate(cnts):
    print("Drawing contour #{}".format(i + 1))
    cv2.drawContours(clone, [c], -1, (0, 255, 0), 2)
    cv2.imshow("Normal Contours", clone)
cv2.waitKey(0)

for(i, c) in enumerate(cnts):
    print("Drawing contour #{}".format(i + 1))
    cv2.drawContours(clone, hull, i, (0, 255, 0), 2)
    cv2.imshow("Hull Contours", clone)
cv2.waitKey(0)
