import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the input image")
ap.add_argument("-s", "--scale", type=float, default=1.5, help="scale factor size")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])


def pyramid(img, scale=1.5, min_size=(30, 30)):
    yield img
    while True:
        w = int(img.shape[1]/scale)
        img = imutils.resize(img, width=w)
        if img.shape[0] < min_size[1] or img.shape[1] < min_size[0]:
            break
        yield img

        for(i, layer) in enumerate(pyramid(img, scale=args["scale"])):
            cv2.imshow("Layer {}".format(i+1), layer)

    cv2.waitKey(0)
