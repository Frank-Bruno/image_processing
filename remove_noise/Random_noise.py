import cv2
from skimage.util import random_noise
from skimage.util import img_as_ubyte
from pathlib import Path

def creating_noise(path=Path):
    im_original = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
        
    sp_noise_01 = random_noise(im_original, mode='s&p', seed=None, clip=True, salt_vs_pepper=0.06)
    sp_noise_02 = random_noise(im_original, mode='s&p', seed=None, clip=True, salt_vs_pepper=0.005)
    gauss_noise_01 = random_noise(im_original, mode='gaussian', seed=None, clip=True, var=0.001)
    gauss_noise_02 = random_noise(im_original, mode='gaussian', seed=None, clip=True, var=0.03)
        
    cv2.imwrite(str(Path(path.parent,"imgs_original",path.stem+"_img_original.png")), im_original)
    cv2.imwrite(str(Path(path.parent,"imgs_noise",path.stem+"_01.png")), img_as_ubyte(sp_noise_01))
    cv2.imwrite(str(Path(path.parent,"imgs_noise",path.stem+"_02.png")), img_as_ubyte(sp_noise_02))
    cv2.imwrite(str(Path(path.parent,"imgs_noise",path.stem+"_03.png")), img_as_ubyte(gauss_noise_01))
    cv2.imwrite(str(Path(path.parent,"imgs_noise",path.stem+"_04.png")), img_as_ubyte(gauss_noise_02))


path = Path(r'/home/frank/git/image_processing/Imagens')
lista = list(path.iterdir())
for p in path.iterdir():
    if p.is_file():
        creating_noise(p)
                