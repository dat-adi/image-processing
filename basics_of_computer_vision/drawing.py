# importing the numpy module to create a canvas of 0 value pixels.
import numpy as np

# importing the OpenCV module
import cv2

# setting up a black canvas of 900 pixels
canvas = np.zeros((300, 300, 3), dtype="uint8")

# setting the color green to a variable.
green = (0, 255, 0)

# To draw a green line across the canvas whose size you have to adjust through the editor?
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draws a three-inch red line across the other diagonal
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# While this command draws a rectangle given the right dimensions
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draws a rectangle when specified the co-ordinates, with a thickness for the edges
cv2.rectangle(canvas, (20, 20), (70, 70), red, 5)
cv2.imshow("Canvas Red", canvas)
# The duration for which the canvas stays by the defined value
cv2.waitKey(0)

blue = (255, 0, 0)
# -1 thickness causes the entire box to get filled.
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas Blue", canvas)
cv2.waitKey(0)

# centers the canvas to the center and forms rings based on the increment of the radius
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (int(canvas.shape[1] / 2), int(canvas.shape[0] / 2))
white = (255, 255, 255)
for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)
cv2.imshow("Canvas White", canvas)
cv2.waitKey(0)

for i in range(0, 25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,))
    cv2.circle(canvas, tuple(pt), radius, color, -1)

    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)

image = cv2.imread(
        "~/Code/image-processing/assets/ey.jpg"
)
cv2.circle(image, (168, 188), 90, (0, 0, 255), -2)
cv2.circle(image, (150, 164), 10, (0, 0, 255), -1)
cv2.circle(image, (192, 174), 10, (0, 0, 255), -1)
cv2.rectangle(image, (134, 200), (186, 218), (0, 0, 255), -1)

# showing the output of the process
cv2.imshow("Output", image)
cv2.waitKey(0)
