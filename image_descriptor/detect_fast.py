"""
import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

detector = cv2.xfeatures2d.SIFT_create()
kps = detector.detect(gray)
print("Number of key points : {}".format(len(kps)))

for kp in kps:
    r = int(0.5*kp.size)
    (x, y) = np.int0(kp.pt)
    cv2.circle(image, (x, y), r, (0, 255, 255), 2)

cv2.imshow("Images", np.hstack([orig, image]))
cv2.waitKey(0)
"""

import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()

# find and draw the keypoints
kp = fast.detect(gray, None)

# Print all default params
print("Threshold: ", fast.getThreshold())
print("nonmaxSuppression: ", fast.getNonmaxSuppression())
print("neighborhood: ", fast.getType())
print("Total Keypoints with nonmaxSuppression: ", len(kp))

# Disable nonmaxSuppression
fast.setNonmaxSuppression(False)
kp = fast.detect(gray, None)
print("Total Keypoints without nonmaxSuppression: ", len(kp))

# Output the points on the mats
img2 = cv2.drawKeypoints(image, kp, None, color=(128, 0, 0))
img3 = cv2.drawKeypoints(image, kp, None, color=(0, 0, 128))

# Show the mats
cv2.imshow("img1", image)  # Original mat
cv2.imshow("img2", img2)  # With nonmaxSuppression
cv2.imshow("img3", img3)  # Without nonmaxSuppression
cv2.waitKey()
