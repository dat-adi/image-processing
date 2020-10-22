# we are using logistic regression to train the model.
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
import numpy as np
import imutils
import cv2

print("[INFO] fetching data...")
dataset = datasets.fetch_lfw_people(min_faces_per_person=70, funneled=True, resize=0.5)
(trainData, testData, trainLabels, testLabels) = train_test_split(
    dataset.data, dataset.target, test_size=0.25, random_state=42
)

print("[INFO] training model...")
model = LogisticRegression()
model.fit(trainData, trainLabels)
print(
    classification_report(
        testLabels, model.predict(testData), target_names=dataset.target_name
    )
)

for i in np.random.randint(0, high=testLabels.shape[0], size=(10,)):
    image = testData[i].reshape((62, 47))
    name = dataset.target_names(testLabels[i])
    image = imutils.resize(
        image.astype("uint8"), width=image.shape[1] * 3, inter=cv2.INTER_CUBIC
    )

    prediction = model.predict(testData[i].reshape(1, -1))[0]
    prediction = dataset.target_names[prediction]
    print("[PREDICTION] predicted : {}, actual: {}".format(prediction, name))
    cv2.imshow("Face", image)
    cv2.waitKey(0)
