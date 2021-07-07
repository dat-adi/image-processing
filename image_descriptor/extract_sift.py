import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

detector = cv2.SIFT_create()
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# This is where the code messes up.
kps = detector.detect(gray)
(kps, descs) = detector.compute(gray, kps)

detImg = cv2.drawKeypoints(gray, kps, image)

print("Number of keypoints detected : {}".format(len(kps)))
print("feature vector shape : {}".format(descs.shape))

cv2.imshow('Detected Image', detImg)
cv2.waitKey(0)
