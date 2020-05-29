import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("Original", image)

print("Width", image.shape[1])
print("Height", image.shape[0])
face = image[:400, :600]
cv2.imshow("Face", face)
cv2.waitKey(0)

body = image[400:600, 120:600]
cv2.imshow("Body", body)
cv2.waitKey(0)
