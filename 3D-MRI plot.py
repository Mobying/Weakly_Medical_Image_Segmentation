import matplotlib
import numpy as np

matplotlib.use('TkAgg')

from matplotlib import pylab as plt
import nibabel as nib
from nibabel import nifti1
from nibabel.viewers import OrthoSlicer3D


# path = 'ADNI_136_S_0429_MR_MPR-R__GradWarp__B1_Correction__N3__Scaled_Br_20070215220055664_S15534_I40387.nii'

modality = 't1ce'
# path = 'data/preprocessed/BraTS19_2013_2_1/' + modality + '.nii.gz'
path = 'data/original/BraTS19_2013_2_1/BraTS19_2013_2_1_' + modality + '.nii.gz'
# path = nib.load('data/original/BraTS19_2013_2_1/BraTS19_2013_2_1_t1.nii.gz'
# path = nib.load('data/original/BraTS19_2013_2_1/BraTS19_2013_2_1_flair.nii.gz'

# 翻转180度：
def flip180(arr):
    new_arr = arr.reshape(arr.size)
    new_arr = new_arr[::-1]
    new_arr = new_arr.reshape(arr.shape)
    return new_arr


# 向左翻转90度：
def flip90_left(arr):
    new_arr = np.transpose(arr)
    new_arr = new_arr[::-1]
    return new_arr


# 向右翻转90度：
def flip90_right(arr):
    new_arr = arr.reshape(arr.size)
    new_arr = new_arr[::-1]
    new_arr = new_arr.reshape(arr.shape)
    new_arr = np.transpose(new_arr)[::-1]
    return new_arr

# 垂直镜像/上下翻转
def flip_ud(arr):
    return np.flipud(arr)

# 水平镜像/左右翻转
def flip_lr(arr):
    return np.fliplr(arr)


img = nib.load(path)
img_arr = img.get_fdata()
if img.dataobj.shape[2] == 155:
    img_arr = flip_lr(img_arr)  # Brats
else:
    img_arr = flip90_right(img_arr)  # ADNI

img = nib.Nifti1Image(img_arr, affine=None)

# print(img)
# print(img.header['db_name'])  # 输出头信息

width, height, queue = img.dataobj.shape
print(img.dataobj.shape)

title = modality
plot = OrthoSlicer3D(img.dataobj, axes=None, title=title)

# plot = OrthoSlicer3D(img.dataobj,title='ADNI')
plot.set_position(113, 133, 101)
plot._plt.savefig(title + '.png')
# plot.show()

# OrthoSlicer3D(img.dataobj,title='t1ce').show()


# num = 1
# for i in range(0, queue, 10):
#     img_arr = img.dataobj[:, :, i]
#     plt.subplot(5, 4, num)
#     plt.imshow(img_arr, cmap='gray')
#     num += 1
#
#
# plt.show()