import os

from skimage import io, data, color
import matplotlib.pyplot as plt
import numpy as np
from cv2 import imread

# image = data.chelsea()
# <class 'numpy.ndarray'>
# print(type(image))

image_dir = 'PNG2'

plane_dir_list = ['Sagittal', 'Coronal', 'Transverse']
plane_dir_index = 2
plane = plane_dir_list[plane_dir_index]

# image = color.rgb2gray(io.imread(image_dir + '/processed/t1ce/101.png'))
image = imread(os.path.join(image_dir, 'preprocessed/Transverse/t1ce/101.png'))
# image = imread(os.path.join(image_dir, 'preprocessed/Coronal/t1ce/144.png'))
# image = imread(os.path.join(image_dir, 'preprocessed/Sagittal/t1ce/105.png'))
# print(type(image))  # <class 'numpy.ndarray'>
# # image = imread(os.path.join(image_dir + '/processed/t2/101.png'))
# mask = imread(os.path.join(image_dir + '/processed/truth/101.png'))
mask = imread(os.path.join(image_dir + '/preprocessed/Transverse/truth/101.png'))
# mask = imread(os.path.join(image_dir + '/preprocessed/Coronal/truth/144.png'))
# mask = imread(os.path.join(image_dir + '/preprocessed/Sagittal/truth/105.png'))
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

label_image = color.label2rgb(labels, bg_label=0)
label_overlay = color.label2rgb(labels, image=image, bg_label=0)
plt.figure(figsize=(12, 12), facecolor='black', edgecolor='black')
plt.subplot(2, 2, 1)
plt.imshow(mask)
plt.axis('off')
title_obj = plt.title('Original Label', size=30, y=0.01)
plt.setp(title_obj, color='white')

plt.subplot(2, 2, 2)
plt.imshow(image)
plt.axis('off')
title_obj = plt.title('Original Image', size=30, y=0.01)
plt.setp(title_obj, color='white')

plt.subplot(2, 2, 3)
plt.imshow(label_image)
plt.axis('off')
title_obj = plt.title('Label Colored', size=30, y=0.01)
plt.setp(title_obj, color='white')

plt.subplot(2, 2, 4)
plt.imshow(label_overlay)
plt.axis('off')
title_obj = plt.title('Label Overlay Colored', size=30, y=0.01)
plt.setp(title_obj, color='white')

# io.imshow(label_image)
# fig = plt.gcf()
# fig.set_facecolor('black')
plt.subplots_adjust(wspace=0, hspace=0)
plt.tight_layout(pad=0)
# axes = plt.gca()
# axes.set_color('black')
plt.savefig('test_plot/' + plane + '/label_overlay_colored_compare.png')
plt.show()
plt.close()