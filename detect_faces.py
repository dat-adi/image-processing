import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required=True, help="Path to where the face cascade resides")
ap.add_argument("-i", "--image", required=True, help="Path to where the image file resides")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

detector = cv2.CascadeClassifier(args["face"])
faceRects = detector.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, minSize=(30, 30),
                                      flags=cv2.CV_HAAR_SCALE_IMAGE)  # CV_HAAR_SCALE_IMAGE changed
print(" Found {} face(s)".format(len(faceRects)))

for(x, y, w, h) in faceRects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Faces", image)
cv2.waitKey(0)
