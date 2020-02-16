from scipy.spatial import distance as dist
from imutils import paths
import numpy as np
import cv2

imagePaths = sorted(list(paths.list_images("D:\\Learning\\ImageProcessing\\Coconut_trees")))
index = {}

for imagePath in imagePaths:
    image = cv2.imread(imagePath)
    filename = imagePath[imagePath.rfind("/") + 1:]
    (means, stds) = cv2.meanStdDev(image)
    features = np.concatenate([means, stds]).flatten()
    index[filename] = features

query = cv2.imread(imagePaths[0])
cv2.imshow("Query (coco1.jpg)", query)
keys = sorted(index.keys())

for (i, k) in enumerate(keys):
    if k == "coco1.jpg":
        continue

    image = cv2.imread(imagePaths[i])
    d = dist.euclidean(index[imagePaths[0]], index[k])
    cv2.putText(image, "{}".format(d), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    cv2.imshow(k, image)
cv2.waitKey(0)
