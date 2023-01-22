#https://www.geeksforgeeks.org/spatial-filters-averaging-filter-and-median-filter-in-image-processing/
# Median Spatial Domain Filtering
import cv2
import numpy as np

# Read the image
img = cv2.imread("/home/frank/github_repositorios/image_processing/Imagens/moon.png",cv2.IMREAD_GRAYSCALE)

# Obtain the number of rows and columns
# of the image
m, n = img.shape
alfa=0
kernel = np.array([[-alfa,alfa+1,-alfa],[alfa+1, alfa-4, alfa+1],[-alfa, alfa+1, -alfa]], dtype=float) #* (1/(alfa+1))

# Traverse the image. For every 3X3 area,
# find the median of the pixels and
# replace the center pixel by the median
img_new = np.zeros([m, n])
img_mask = np.zeros([m, n])
kernerl_size = 3
k = int(kernerl_size/2)
temp = np.zeros([kernerl_size, kernerl_size])


for i in range(k, m-k):
    for j in range(k, n-k):
        for l in range (0,kernerl_size):
            for c in range(0,kernerl_size):
                temp[l,c] = img[i-k+l, j-k+c]*kernel[l,c]
        img_mask[i, j]= np.sum(temp)

img_mask = img_mask.astype(np.uint8)
#img_mask2 = cv2.subtract(img, img_mask)
#img_mask = img - img_mask
#for i in range(0, m):
#    for j in range(0, n):
#        img_mask[i,j] = img[i,j]-img_mask[i,j]
#        img_new[i,j] = img[i,j] + 2*img_mask[i,j]

#img_new = img + 2*img_mask
#img_new2 = cv2.add(img,2*img_mask2)
#img_mask = img_mask.astype(np.uint8)
img_new = img_new.astype(np.uint8)
cv2.imshow("original",img)
#cv2.imshow("Mask",img_mask)
cv2.imshow("Img filtering",img_mask)
#cv2.imshow("Img filtering2",img_new2)

cv2.waitKey()
#cv2.imwrite('moon_teste_median.png', img_new)
