import numpy as np
import cv2 
from pathlib import Path
from math import log10

def filtering_images(path=Path):
    M = [3, 5, 7]
    img_original = cv2.imread(str(path), -1)

    for version in range(1,5):
        noise_img_name = str(path.name)[:str(path.name).find("_img")]+"_0"+str(version)
        path_img_noise= Path(path.parents[1],"imgs_noise",noise_img_name+".png")
        noise_image = cv2.imread(str(path_img_noise), -1)
        print("For noise image version = ", version)
        print("Noise image(no filtering) PSNR = ", calculate_erro(img_original, noise_image))

        for i in M:
            averaging = cv2.blur(img_original,(i,i))
            cv2.imwrite(str(Path(path.parents[1],"imgs_filtering", noise_img_name+"_0"+str(i)+"avr"+".png")),averaging)
            median = cv2.medianBlur(img_original, i) 
            cv2.imwrite(str(Path(path.parents[1],"imgs_filtering", noise_img_name+"_0"+str(i)+"median"+".png")),median)
            print("M = "+str(i)+", PSNRs: average="+str(calculate_erro(img_original, averaging)) + ", median=" + str(calculate_erro(img_original, median)))


def calculate_erro(img_original, img_compared):
    erro = img_original-img_compared
    MSE = np.mean(erro)**2
    PSN = 10*log10((255**2)/MSE)
    return PSN

path = Path(r'/home/frank/Imagens/imgs_original')
lista = list(path.iterdir())
for p in path.iterdir():
    if p.is_file():
        print(p)
        filtering_images(p)
