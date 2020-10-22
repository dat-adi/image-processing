from sklearn.cluster import KMeans
import numpy as np
import random
import cv2

colors = [
    (138, 8, 8),
    (180, 4, 4),
    (223, 1, 1),
    (255, 0, 0),
    (250, 88, 88),
    (8, 138, 8),
    (4, 180, 4),
    (1, 223, 1),
    (0, 255, 0),
    (46, 254, 46),
    (11, 11, 97),
    (8, 8, 138),
    (4, 4, 180),
    (0, 0, 255),
    (46, 46, 254),
]

canvas = np.ones((400, 600, 3), dtype="uint8") * 255
for y in range(0, 400, 20):
    for x in range(0, 600, 200):
        (dX, dY) = np.random.randint(5, 10, size=(2,))
        r = np.random.randint(5, 8)
        color = random.choice(colors)[::-1]

        cv2.circle(canvas, (x + dX, y + dY), r, color, -1)

canvas = cv2.copyMakeBorder(
    canvas, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=(255, 255, 255)
)

gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)
thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)[1]
(cnts, _) = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

data = []

for c in cnts:
    mask = np.zeros(canvas.shape[:2], dtype="uint8")
    cv2.drawContours(mask, [c], -1, 255, -1)
    features = cv2.mean(canvas, mask=mask)[:3]
    data.append(features)

    clt = KMeans(n_clusters=3)
    clt.fit(data)
    cv2.imshow("Canvas", canvas)

    for i in np.unique(clt.labels_):
        mask = np.zeros(canvas.shape[:2], dtype="uint8")

        for j in np.where(clt.labels_ == i)[0]:
            cv2.drawContours(mask, [cnts[j]], -1, 255, -1)

    cv2.imshow("Cluster", cv2.bitwise_and(canvas, canvas, mask=mask))
    cv2.waitKey(0)
