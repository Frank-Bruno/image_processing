import cv2
import numpy as np
from pathlib import Path

def average_filter(img_path= Path, ksize= int):
    # Read the image
    img = cv2.imread(str(img_path),cv2.IMREAD_GRAYSCALE)
    kernerl_size = ksize                             # M values
    k = int(kernerl_size/2)

    # Obtain the number of rows and columns of the image
    m, n = img.shape
    img_new = np.zeros([m, n])

    # Develop Averaging filter(ksize, ksize) mask
    temp = np.zeros([kernerl_size, kernerl_size])
    
    
    # Convolve the ksize X ksize mask over the image 
    for i in range(k, m-k):
        for j in range(k, n-k):
            for l in range (0,kernerl_size):
                for c in range(0,kernerl_size):
                    temp[l,c] = img[i-k+l, j-k+c]
            mean = np.mean(temp,axis=None) 
            img_new[i, j]= mean
    img_new = img_new.astype(np.uint8)
    
    #cv2.imshow("Original",img)
    #cv2.imshow("averaging"+str(t),img_new)
    #cv2.waitKey()
    
    filter_img_name = str(img_path.name)[:str(img_path.name).find(".png")]+"_0"+str(ksize)+"_avr.png"
    cv2.imwrite(str(Path(img_path.parents[1],"imgs_smooth",filter_img_name)), img_new)
    
def median_filter(img_path= Path, ksize= int):
    # Read the image
    img = cv2.imread(str(img_path),cv2.IMREAD_GRAYSCALE)
    kernerl_size = ksize                             # M values
    k = int(kernerl_size/2)

    # Obtain the number of rows and columns of the image
    m, n = img.shape
    img_new = np.zeros([m, n])
    
    # Develop Averaging filter(ksize, ksize) mask
    temp = np.zeros([kernerl_size, kernerl_size])

    # Convolve the 3X3 mask over the image 
    for i in range(k, m-k):
        for j in range(k, n-k):
            for l in range (0,kernerl_size):
                for c in range(0,kernerl_size):
                    temp[l,c] = img[i-k+l, j-k+c]

            median = np.median(np.sort(temp, axis= None)) 
            img_new[i, j]= median
            
    img_new = img_new.astype(np.uint8)
    #cv2.imshow("averaging",img_new)
    #cv2.waitKey()
    #cv2.imwrite('moon_teste2_averaging.png', img_new)
    
    filter_img_name = str(img_path.name)[:str(img_path.name).find(".png")]+"_0"+str(ksize)+"_median.png"
    cv2.imwrite(str(Path(img_path.parents[1],"imgs_smooth",filter_img_name)), img_new)

def calculate_PSNR(img_path= Path):
    # Read the image
    img = cv2.imread(str(Path(img_path.parents[1],"imgs_original")),cv2.IMREAD_GRAYSCALE)


path = Path(r'/home/frank/git/image_processing/Imagens/imgs_noise')
lista = list(path.iterdir())
for p in path.iterdir():
    if p.is_file():
        print(p)
        average_filter(p, 3)
        median_filter(p, 3)