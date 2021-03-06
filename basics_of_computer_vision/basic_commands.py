import cv2

image = cv2.imread(
    "C:/Users/narui/OneDrive/Pictures/Wallpapers/cropped-1920-1080-993443.png"
)
print("Type of the image : ", type(image))
print()
print("Shape of the image : {}".format(image.shape))
print("Image Height {}".format(image.shape[0]))
print("Image Width {}".format(image.shape[1]))
print("Dimension of Image {}".format(image.ndim))
print()
print("Image size {}".format(image.size))
print("Maximum RGB value in this image {}".format(image.max()))
print("Minimum RGB value in this image {}".format(image.min()))
print()
print("Value of only R channel {}".format(image[100, 50, 0]))
print("Value of only G channel {}".format(image[100, 50, 1]))
print("Value of only B channel {}".format(image[100, 50, 2]))
