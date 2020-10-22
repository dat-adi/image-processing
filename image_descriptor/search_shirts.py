from imutils import paths
import numpy as np
import cv2
import argparse
from skimage import feature

ap = argparse.ArgumentParser()
ap.add_argument(
    "-d", "--dataset", required=True, help="Path to the dataset of shirt image"
)
ap.add_argument("-q", "--query", required=True, help="Path to the query image")
args = vars(ap.parse_args())

index = {}
radius = 8
numPoints = 24


def describe(image, eps=1e-7):
    lbp = feature.local_binary_pattern(image, numPoints, radius, method="uniform")
    (hist, _) = np.histogram(
        lbp.ravel(), bins=range(0, numPoints + 3), range=(0, numPoints + 2)
    )
    hist = hist.astype("float")
    hist /= hist.sum() + eps

    return hist


for imagePath in paths.list_images(args["dataset"]):
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = describe(gray)

    imagePath = imagePath.replace("\\", "/")
    filename = imagePath[imagePath.rfind("/") + 1 :]
    index[filename] = hist

    query = cv2.imread(args["query"])
    queryFeatures = describe(cv2.cvtColor(query, cv2.COLOR_BGR2GRAY))

    cv2.imshow("Query", query)
    results = {}

    for (k, features) in index.items():
        d = 0.5 * np.sum(
            ((features - queryFeatures) ** 2 / (features + queryFeatures + 1e-10))
        )
        results[k] = d

    results = sorted([(v, k) for (k, v) in results.items()])[:3]

    for (i, (score, filename)) in enumerate(results):
        print("{}, {}, {}".format(i + 1, filename, score))
        image = cv2.imread(args["dataset"] + "/" + filename)
        cv2.imshow("Results {}".format(i + 1), image)

        cv2.waitKey(0)
