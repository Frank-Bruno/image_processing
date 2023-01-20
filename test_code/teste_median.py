#https://www.geeksforgeeks.org/spatial-filters-averaging-filter-and-median-filter-in-image-processing/
# Median Spatial Domain Filtering
import cv2
import numpy as np

# Read the image
img = cv2.imread("/home/frank/git/image_processing/Imagens/imgs_noise/moon_01.png",cv2.COLOR_BGR2GRAY)

# Obtain the number of rows and columns
# of the image
m, n = img.shape

# Traverse the image. For every 3X3 area,
# find the median of the pixels and
# replace the center pixel by the median
img_new = np.zeros([m, n])
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
        img_new[i, j]= np.median(np.sort(temp, axis= None))      
img_new = img_new.astype(np.uint8)
cv2.imshow("median",img_new)
cv2.waitKey()
cv2.imwrite('moon_teste_median.png', img_new)
