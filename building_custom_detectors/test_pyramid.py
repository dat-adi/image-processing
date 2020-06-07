import argparse
import cv2
import imutils


def pyramid(image, scale=1.5, min_size=(30, 30)):
    yield image
    while True:
        w = int(image.shape[1]/scale)
        image = imutils.resize(image, width=w)
        print('3')
        if image.shape[0] < min_size[1] or image.shape[1] < min_size[0]:
            break
        yield image

        for(i, layer) in enumerate(pyramid(image, scale=args["scale"])):
            cv2.imshow("Layer {}".format(i+1), layer)

        cv2.waitKey(0)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the input image")
    ap.add_argument("-s", "--scale", type=float, default=1.5, help="scale factor size")
    args = vars(ap.parse_args())
    image = cv2.imread(args["image"])

    pyramid(image)
