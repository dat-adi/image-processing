import cv2

def save_image(image):
    name = input("What's the name for this saved image?\n")
    cv2.imwrite(name + ".jpg", image)
