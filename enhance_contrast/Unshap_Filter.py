import numpy as np
import cv2

img = cv2.imread('/home/frank/git/image_processing/Imagens/moon.png')

alfa=0.2
kernel = np.array([[-alfa,alfa-1,-alfa],[alfa-1, alfa+5, alfa-1],[-alfa, alfa-1, -alfa]]) * (1/(alfa+1))

img_unsharp = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original Image", img)
cv2.imshow("Filtered Image", img_unsharp)
cv2.imwrite("moon_unsharp.png", img_unsharp)
cv2.waitKey()
