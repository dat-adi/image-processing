# importing OpenCV into the script.
import cv2

# Reading the image location using a hardcoded path
# and using cv2.imread to read the image
image = cv2.imread(
    "C:\\Users\\narui\\PycharmProjects\\image-processing\\assets\\ey.jpg"
)

# printing out the dimensions of the image
print("width: ", image.shape[1])
print("height: ", image.shape[0])
print("channels: ", image.shape[2])

# Displaying the image using the cv2.imshow method
cv2.imshow("Image", image)

# Displays the image until the user presses a key closing the display
cv2.waitKey(0)
