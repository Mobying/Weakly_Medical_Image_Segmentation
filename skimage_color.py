import os

from skimage import io, data, color
import matplotlib.pyplot as plt
import numpy as np
from cv2 import imread

# image = data.chelsea()
# <class 'numpy.ndarray'>
# print(type(image))

image_dir = 'PNG'
#
# image = color.rgb2gray(io.imread(image_dir + '/processed/t1ce/101.png'))
image = imread(os.path.join(image_dir + '/processed/t1ce/101.png'))
# print(type(image))  # <class 'numpy.ndarray'>
# # image = imread(os.path.join(image_dir + '/processed/t2/101.png'))
mask = imread(os.path.join(image_dir + '/processed/truth/101.png'))

# print(type(mask), '\n', np.max(mask), mask.dtype)  # <class 'numpy.ndarray'>, 4 uint8

image_grey = color.rgb2gray(image)
rows, cols = image_grey.shape
labels = np.zeros([rows, cols])
for i in range(rows):
    for j in range(cols):
        if image_grey[i, j] >0.66:
            labels[i, j] = 0
        elif image_grey[i, j] > 0.33:
            labels[i, j] = 1
        else:
            labels[i, j] = 2
label_image = color.label2rgb(labels)
io.imshow(label_image)
io.show()