#https://www.geeksforgeeks.org/spatial-filters-averaging-filter-and-median-filter-in-image-processing/
# Median Spatial Domain Filtering
import cv2
import numpy as np

# Read the image
img = cv2.imread("/home/frank/github_repositorios/image_processing/Imagens/imgs_original/moon_img_original.png",cv2.COLOR_BGR2GRAY)

# Obtain the number of rows and columns
# of the image
m, n = img.shape

# Traverse the image. For every 3X3 area,
# find the median of the pixels and
# replace the center pixel by the median
img_new = np.zeros([m, n])
img_median = np.zeros([m, n])
img_mask = np.zeros([m, n])
kernerl_size = 3
k = int(kernerl_size/2)
temp = np.zeros([kernerl_size, kernerl_size])

for i in range(k, m-k):
    for j in range(k, n-k):
        for l in range (0,kernerl_size):
            for c in range(0,kernerl_size):
                temp[l,c] = img[i-k+l, j-k+c]
                
                # for a in range(-k, k+1):
                #     for b in range(-k, k+1):
                #         temp[l,c] = img[i+a, j+b]
                        
                        

        #temp = np.sort(temp, axis= None)
        img_median[i, j]= np.median(np.sort(temp, axis= None))      
img_median = img_median.astype(np.uint8)
img_mask = cv2.subtract(img , img_median)
for i in range(0, m):
    for j in range(0, n):
        #img_mask[i,j] = img[i,j]-img_median[i,j]
        img_new[i,j] = img[i,j] + 3*img_mask[i,j]

img_new2 = cv2.add(img,3*img_mask)
img_mask = img_mask.astype(np.uint8)
img_new = img_new.astype(np.uint8)

cv2.imshow("original",img)
cv2.imshow("Mask",img_mask)
cv2.imshow("Mask2",img_new2)
cv2.imshow("Img filtering",img_new)

cv2.waitKey()
#cv2.imwrite('moon_teste_median.png', img_new)
