# coding=utf-8
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2  
image = mpimg.imread('exit-ramp.jpg')
plt.imshow(image)

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #grayscale conversion
plt.imshow(gray, cmap='gray')


low_t = 80
high_t = 170
kernel_size = (3,3)

blur_gray =  cv2.GaussianBlur(gray,kernel_size,0)
# o algotimo vai primeiro a threshold elevado e procura os gradients mais fortes
# rejeitando os abaixo do threshold inferior
# De seguida, os pixeis entre o low e o high são mantidos desde que estejam ligados so edge forte definido anteriormente
# Devolve uma imagem toda preta com os edges fortes a branco
edges = cv2.Canny(blur_gray,low_t,high_t)
plt.imshow(edges,cmap='Greys_r')


cv2.imshow("edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()