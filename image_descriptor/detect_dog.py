import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d_SIFT()
kp = sift.detect(gray, None)
print("Key points : {}".format(len(kp)))

for k in kp:
    r = int(0.5*k.size)
    (x, y) = np.int0(k.pt)
    cv2.circle(image, x, y, r, (0, 255, 255), 2)

cv2.imshow("Images", np.hstack([orig, image]))

image = cv2.drawKeypoints(gray, kp, image, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Detecting key points", image)
cv2.waitKey(0)
