# importing numpy to work with pixels
import numpy as np

# importing the OpenCV module
import cv2

# creating a square of zeros using a variable
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle : ", rectangle)

# creating a circle of zeros using a variable
circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle : ", circle)

# the bitwise_and function executes the AND operation
# on both the images
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

# the bitwise_or function executes the OR operation
# on both the images
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

# the bitwise_xor function executes the XOR operation
# on both the images
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

# the bitwise_not function executes the NOT operation
# on both the images
bitwiseNot = cv2.bitwise_not(rectangle, circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)
