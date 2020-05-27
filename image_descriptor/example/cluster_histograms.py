from sklearn.cluster import KMeans
from imutils import paths
import numpy as np
import argparse
import cv2


class LabHistograms:
    def __init__(self, bins):
        self.bins = bins

    def describe(self, image, mask=None):
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        hist = cv2.calcHist([lab], [0, 1, 2], mask, self.bins, [0, 256, 0, 256, 0, 256])
        hist = cv2.normalize(hist, None).flatten()

        return hist


def describe(image, mask=None):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    hist = cv2.calcHist([lab], [0, 1, 2], mask, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, None).flatten()
    return hist


ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="Path to the input data set directory")
ap.add_argument("-k", "--clusters", type=int, default=2, help="Number of clusters to generate")
args = vars(ap.parse_args())

desc = LabHistograms([8, 8, 8])
data = []

imagePaths = list(paths.list_images(args["dataset"]))
imagePaths = np.array(sorted(imagePaths))

for imagePath in imagePaths:
    image = cv2.imread(imagePath)
    hist = describe(image)
    data.append(hist)

clt = KMeans(n_clusters=args["clusters"])
labels = clt.fit_predict(data)

for label in np.unique(labels):
    labelPaths = imagePaths[np.where(labels == label)]

for (i, path) in enumerate(labelPaths):
    image = cv2.imread(path)
    cv2.imshow("Cluster {}, Image{}".format(label+1, i+1), image)

cv2.waitKey(0)
cv2.destroyAllWindows()

