import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

image = mpimg.imread('test.jpg')
print('IMG : ',type(image), 'DIMS : ',image.shape)

ysize = image.shape[0]
xsize = image.shape[1]

color_select = np.copy(image)

plt.imshow(image)

red_t = 195
blue_t = 195
green_t = 195

rgb_threshold =  [red_t,green_t,blue_t]

thresholds = (image[:,:,0] < rgb_threshold[0] ) | (image[:,:,1] < rgb_threshold[1]) | (image[:,:,2] < rgb_threshold[2])

color_select[thresholds] = [0,0,0]

plt.imshow(color_select)
plt.show()
