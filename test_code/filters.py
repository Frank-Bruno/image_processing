import cv2
import numpy as np

# Read the image
img = cv2.imread("/home/frank/git/image_processing/Imagens/imgs_noise/moon_01.png",cv2.COLOR_BGR2GRAY)

# Obtain the number of rows and columns
# of the image
m, n = img.shape

# Develop Averaging filter(3, 3) mask

# Convolve the kxk mask over the image 
img_new = np.zeros([m, n])
kernerl_size = [3,5,7]                              # M values
#k = np.zeros([len(kernerl_size)])
for t in range (0,len(kernerl_size)):
    k = int(kernerl_size[t]/2)

    temp = np.zeros([kernerl_size[t], kernerl_size[t]])
    for i in range(k, m-k):
        for j in range(k, n-k):
            for l in range (0,kernerl_size[t]):
                for c in range(0,kernerl_size[t]):
                    temp[l,c] = img[i-k+l, j-k+c]

            median = np.mean(temp,axis=None) 
            img_new[i, j]= median

    img_new = img_new.astype(np.uint8)

    #cv2.imshow("Original",img)
    #cv2.imshow("averaging"+str(t),img_new)
    #cv2.waitKey()
    cv2.imwrite('moon_teste_averaging'+str(t)+'.png', img_new)