import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="C:/Users/narui/OneDrive/Pictures/Wallpapers/cropped-1920-1080-993443.png")
args = vars(ap.parse_args())

image = cv2.imread("C:/Users/narui/OneDrive/Pictures/Wallpapers/cropped-1920-1080-993443.png")
cv2.imshow("Original", image)


M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)


def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted
