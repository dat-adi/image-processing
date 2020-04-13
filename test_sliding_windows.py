import argparse
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to input image")
ap.add_argument("-w", "--width", type=int, help="Width to sliding windows")
ap.add_argument("-t", "--height", type=int, help="height to sliding windows")
ap.add_argument("-s", "--scale", type=float, default=1.5, help="scale factor size")
args = vars(ap.parse_args())


def sliding_windows(image, stepSize, windowSize):
    for y in range(0, image.shape[0], stepSize):
        for x in range(0, image.shape[1], stepSize):
            yield(x, y, image[y:y + windowSize[1], x:x + windowSize[0]])


image = cv2.imread(args["image"])
(winW, winH) = (args["width"], args["height"])

for layer in pyramid(image, scale=args["scale"]):
    for(x, y, window) in sliding_windows(layer, stepSize=32, windowSize=(winW, winH)):
        if window.shape[0] != winH or window.shape[1] != winW:
            continue

        clone = layer.copy()
        cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
        cv2.imshow("Window", clone)

cv2.waitKey(1)
time.sleep(0.025)
