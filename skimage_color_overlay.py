import os

from skimage import io, data, color
import matplotlib.pyplot as plt
import numpy as np
from cv2 import imread

# image = data.chelsea()
# <class 'numpy.ndarray'>
# print(type(image))

image_dir = 'PNG2'
#
# image = color.rgb2gray(io.imread(image_dir + '/processed/t1ce/101.png'))
image = imread(os.path.join(image_dir, 'preprocessed/Transverse/t1ce/101.png'))
# print(type(image))  # <class 'numpy.ndarray'>
# # image = imread(os.path.join(image_dir + '/processed/t2/101.png'))
# mask = imread(os.path.join(image_dir + '/processed/truth/101.png'))
mask = imread(os.path.join(image_dir + '/preprocessed/Transverse/truth/101.png'))
# print(type(mask), '\n', np.max(mask))
#
print(type(mask), '\n', np.max(mask), mask.dtype)  # <class 'numpy.ndarray'>, 4 uint8
mask_gray = color.rgb2gray(mask)
rows, cols = mask_gray.shape
labels = np.zeros([rows, cols])
for i in range(rows):
    for j in range(cols):
        if mask_gray[i, j] > 0.66:
        # if mask_gray[i, j] == 1:
            labels[i, j] = 2
        elif mask_gray[i, j] > 0.33:
        # elif mask_gray[i, j] > 0.4980392155:
        # elif mask_gray[i, j] == 0.4980395:
            labels[i, j] = 3
        elif mask_gray[i, j] > 0:
            labels[i, j] = 1
label_image = color.label2rgb(labels, image=image, bg_label=0)
plt.figure(figsize=(6, 6), facecolor='black', edgecolor='black')
plt.imshow(label_image)
# io.imshow(label_image)
plt.axis('off')
title_obj = plt.title('Label Overlay Colored', size=20, y=0.01)
# title_obj = plt.title('label_colored', size=20, y=-0.2)
plt.setp(title_obj, color='white')
# fig = plt.gcf()
# fig.set_facecolor('black')
# plt.subplots_adjust(wspace=0, hspace=0)
plt.tight_layout(pad=0)
# axes = plt.gca()
# axes.set_color('black')
plt.savefig('test_plot/label_overlay_colored.png')
plt.show()