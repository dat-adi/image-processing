import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image.")
args = vars(ap.parse_args())

image = cv2.imread("ey.jpg")
cv2.imshow("Original", image)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask,(0, 90), (290, 450), 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask applied to Image", masked)
cv2.waitKey(0)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (145, 200), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask", mask)
cv2.imshow("Mask applied to Image", masked)
cv2.waitKey(0)
