from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.svm import SVC
import numpy as np

tl = np.random.uniform(size=(100, 2)) + np.array([-2.0, 2.0])
tr = np.random.uniform(size=(100, 2)) + np.array([2.0, 2.0])
br = np.random.uniform(size=(100, 2)) + np.array([2.0, -2.0])
bl = np.random.uniform(size=(100, 2)) + np.array([-2.0, -2.0])
X = np.vstack([tl, tr, br, bl])
y = np.hstack([[1] * len(tl), [-1] * len(tr), [1] * len(br), [-1] * len(bl)])

(trainData, testData, trainLabels, testLabels) = train_test_split(
    X, y, test_size=0.25, random_state=42
)

print("[RESULTS] SVM w/ Linear Kernel")
model = SVC(kernel="linear")
model.fit(trainData, trainLabels)
print(classification_report(testLabels, model.predict(testData)))
print("")

print("[RESULTS] SVM w/ Polynomial Kernel")
model = SVC(kernel="poly", degree=2, coef0=1)
model.fit(trainData, trainLabels)
print(classification_report(testLabels, model.predict(testData)))
