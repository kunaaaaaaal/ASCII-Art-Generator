# opencv library is used to read and edit pictures.

import numpy as np
import cv2 as cv


img = cv.imread("photo-4.jpg")

# This command is used to print the dimensions of the image([n*m] in case of a grayscale image 
# and [n*m*3] in the case of a colored image)

print(img.shape)

# Code to display the original image.

cv.imshow('wow', img)
cv.waitKey(0)
cv.destroyAllWindows()

# Since we are creating a pencil sketch of the photo, we first convert the original image into a grayscale image.

grey_img=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Code to invert the image.

invert_img=cv.bitwise_not(grey_img)

# Gaussian blur is applied to the image.
# The kernel size of (51,51) is selected by Hit-And-Trial method.

blur_img=cv.GaussianBlur(invert_img, (51,51),0)

# The blurred image is now inverted.

invblur_img=cv.bitwise_not(blur_img)

# The sketch is obtained by performing bitwise division between the grayscale image and the inverted-blurred image.

sketch_img=cv.divide(grey_img,invblur_img, scale=256.0)

# Code to save the sketch.

cv.imwrite('sketch.png', sketch_img)

# Code to display the sketch.

cv.imshow('sketch image',sketch_img)
cv.waitKey(0)
cv.destroyAllWindows()

