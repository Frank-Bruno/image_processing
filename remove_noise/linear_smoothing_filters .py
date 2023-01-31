import cv2
import numpy as np
from pathlib import Path
from math import log10

def smoothing_filter(img_path= Path):
    M_values = [3, 5, 7]
    # Read the image
    img_original = cv2.imread(str(img_path),cv2.IMREAD_GRAYSCALE)

    # Obtain the number of rows and columns of the image
    m, n = img_original.shape
    img_mean = np.zeros([m, n])
    img_median = np.zeros([m, n]) 
    
    for version in range(1,5):
        filter_img_name = str(img_path.name)[:str(img_path.name).find("_img")]+"_0"+str(version)
        print(img_path.name)
        path_img_noise= Path(img_path.parents[1],"imgs_noise",filter_img_name+".png")
        noise_image = cv2.imread(str(path_img_noise), -1)
        print("For noise image version = ", version)
        print("Noise image(no filtering) PSNR = ", calculate_PSNR(img_original, noise_image))
        
        for Msize in M_values:
            kernerl_size = Msize                             # M values
            k = int(kernerl_size/2)
            
            # Develop Averaging filter(Msize, Msize) mask
            temp = np.zeros([kernerl_size, kernerl_size])
            
            # Convolve the  Msize X Msize mask over the image 
            for i in range(k, m-k):
                for j in range(k, n-k):
                    for l in range (0,kernerl_size):
                        for c in range(0,kernerl_size):
                            temp[l,c] = noise_image[i-k+l, j-k+c]
                    mean = np.mean(temp,axis=None) 
                    median = np.median(np.sort(temp, axis= None)) 
                    img_mean[i, j]= mean
                    img_median[i, j]= median

            img_mean = img_mean.astype(np.uint8)
            img_median = img_median.astype(np.uint8)

            #cv2.imshow("Original",img)
            #cv2.imshow("averaging"+str(t),img_mean)
            #cv2.waitKey()

            #filter_img_name = str(img_path.name)[:str(img_path.name).find(".png")]+"_0"+str(Msize)+"_avr.png"
            #filter_img_name = str(img_path.name)[:str(img_path.name).find(".png")]+"_0"+str(Msize)+"_median.png"
            cv2.imwrite(str(Path(img_path.parents[1],"imgs_smooth",filter_img_name+"_0"+str(Msize)+"_avr.png")), img_mean)
            cv2.imwrite(str(Path(img_path.parents[1],"imgs_smooth",filter_img_name+"_0"+str(Msize)+"_median.png")), img_median)

            print("M = "+str(Msize)+", PSNRs: average="+str(calculate_PSNR(img_original, img_mean)) + ", median=" + str(calculate_PSNR(img_original, img_median)))
    
def calculate_PSNR(img_original, img_compared):
    erro = cv2.subtract(img_original, img_compared)
    MSE = np.mean(erro)**2
    PSN = 10*log10((255**2)/MSE)
    return PSN


path = Path(r'/home/frank/git/image_processing/Imagens/imgs_original')
lista = list(path.iterdir())
for p in path.iterdir():
    if p.is_file():
        smoothing_filter(p)