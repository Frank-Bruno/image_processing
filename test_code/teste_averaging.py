# Averaging Spatial Domain Filtering
import cv2
import numpy as np

# Read the image
img = cv2.imread("/home/frank/git/image_processing/Imagens/imgs_noise/moon_01.png",cv2.COLOR_BGR2GRAY)

# Obtain the number of rows and columns
# of the image
m, n = img.shape

# Develop Averaging filter(3, 3) mask
# mask = np.ones([3, 3], dtype = int)
# mask = mask / 9

# Convolve the 3X3 mask over the image 
img_new = np.zeros([m, n])
kernerl_size = 5
k = int(kernerl_size/2)
temp = np.zeros([kernerl_size, kernerl_size])

# for i in range(1, m-1):
#     for j in range(1, n-1):
#         t = img[i-1, j-1]*mask[0, 0]+img[i-1, j]*mask[0, 1]+img[i-1, j + 1]*mask[0, 2]+img[i, j-1]*mask[1, 0]+ img[i, j]*mask[1, 1]+img[i, j + 1]*mask[1, 2]+img[i + 1, j-1]*mask[2, 0]+img[i + 1, j]*mask[2, 1]+img[i + 1, j + 1]*mask[2, 2]
#         img_new[i, j]= t

for i in range(k, m-k):
    for j in range(k, n-k):
        for l in range (0,kernerl_size):
            for c in range(0,kernerl_size):
                temp[l,c] = img[i-k+l, j-k+c]
                                       
                                       
        median = np.mean(temp,axis=None) 
        img_new[i, j]= median
        #img_new[i, j]= temp
img_new = img_new.astype(np.uint8)
cv2.imshow("averaging",img_new)
cv2.waitKey()
cv2.imwrite('moon_teste2_averaging.png', img_new)