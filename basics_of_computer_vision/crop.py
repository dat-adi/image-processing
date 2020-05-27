import cv2

image = cv2.imread("ey.jpg")
cv2.imshow("Original", image)

print("Width", image.shape[1])
print("Height", image.shape[0])
face = image[:400, :600]
cv2.imshow("Face", face)
cv2.waitKey(0)

body = image[400:600, 120:600]
cv2.imshow("Body", body)
cv2.waitKey(0)
