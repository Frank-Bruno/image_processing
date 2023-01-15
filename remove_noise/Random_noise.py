import cv2
from skimage.util import random_noise
from skimage.util import img_as_ubyte
from pathlib import Path

#Class for make noising imagens
class Random_noise:
    def __init__(self, path=Path):
        self.path = path
        self.im_original = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)

    def make_img_noise(self):
        
        sp_noise_01 = random_noise(self.im_original, mode='s&p', seed=None, clip=True, salt_vs_pepper=0.06)
        sp_noise_02 = random_noise(self.im_original, mode='s&p', seed=None, clip=True, salt_vs_pepper=0.005)
        gauss_noise_01 = random_noise(self.im_original, mode='gaussian', seed=None, clip=True, var=0.001)
        gauss_noise_02 = random_noise(self.im_original, mode='gaussian', seed=None, clip=True, var=0.03)

        #sp_noise_01 = np.array(255*sp_noise_01, dtype='uint8')
        # sp_noise_02 = np.array(255*sp_noise_02, dtype='uint8')
        # gauss_noise_01 = np.array(255*gauss_noise_01, dtype='uint8')
        # gauss_noise_02 = np.array(255*gauss_noise_02, dtype='uint8')
        
        cv2.imwrite(str(Path(self.path.parent,"imgs_original",self.path.stem+"_img_original.png")), self.im_original)
        cv2.imwrite(str(Path(self.path.parent,"imgs_noise",self.path.stem+"_01.png")), img_as_ubyte(sp_noise_01))
        cv2.imwrite(str(Path(self.path.parent,"imgs_noise",self.path.stem+"_02.png")), img_as_ubyte(sp_noise_02))
        cv2.imwrite(str(Path(self.path.parent,"imgs_noise",self.path.stem+"_03.png")), img_as_ubyte(gauss_noise_01))
        cv2.imwrite(str(Path(self.path.parent,"imgs_noise",self.path.stem+"_04.png")), img_as_ubyte(gauss_noise_02))


path = Path(r'/home/frank/Imagens')
lista = list(path.iterdir())
for p in path.iterdir():
    if p.is_file():
        l = Random_noise(p)
        l.make_img_noise()
        