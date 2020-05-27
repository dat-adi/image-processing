import cv2  #imports the OpenCV functions into the program.

image = cv2.imread("ey.jpg")
print("width: ", image.shape[1])
print("height: ", image.shape[0])
print("channels: ", image.shape[2])

cv2.imshow("Image", image)
cv2.waitKey(0)

