import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('../../Images/Images_Original/img_1.jpg')
img = cv2.resize(img1, (400,600))
dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(dst)
plt.show()