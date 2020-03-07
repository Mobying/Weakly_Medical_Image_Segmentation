import os

from skimage import io, data, color
import matplotlib.pyplot as plt
import numpy as np
from cv2 import imread

image = data.chelsea()  # <class 'numpy.ndarray'>
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