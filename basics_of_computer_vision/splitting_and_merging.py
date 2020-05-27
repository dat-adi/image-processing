import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(B, G, R) = cv2.split(image)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)

cv2.destroyAllWindows()

zeroes = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([zeroes, zeroes, R]))
cv2.imshow("Green", cv2.merge([zeroes, G, zeroes]))
cv2.imshow("Blue", cv2.merge([B, zeroes, zeroes]))
cv2.waitKey(0)
