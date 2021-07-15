from imutils import paths
import argparse
import dlib
import cv2

ap = argparse.ArgumentParser()
ap.add_argument(
    "-d", "--detector", required=True, help="Path to the trained object detector"
)
ap.add_argument(
    "-t", "--tester", required=True, help="Path to the directory of testing images"
)
args = vars(ap.parse_args())

detector = dlib.simple_object_detector(args["detector"])
for testingPath in paths.list_images(args["tester"]):
    image = cv2.imread(testingPath)
    boxes = detector(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    for b in boxes:
        (x, y, w, h) = (b.left(), b.top(), b.right(), b.bottom())
        cv2.rectangle(image, (x, y), (w, h), (0, 255, 0), 2)

    cv2.imshow("Image", image)
    cv2.waitKey(0)
