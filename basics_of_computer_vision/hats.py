import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)

tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)
cv2.imshow("Original", image)
cv2.imshow("BlackHat", blackhat)
cv2.imshow("TopHat", tophat)
cv2.waitKey(0)
