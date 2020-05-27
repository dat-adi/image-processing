import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

detector = cv2.xfeatures2d_SIFT()
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# This is where the code messes up.
kps = detector.detect(gray)
(kps, descs) = detector.compute(gray, kps)

print("Number of keypoints detected : {}".format(len(kps)))
print("feature vector shape : {}".format(descs.shape))
