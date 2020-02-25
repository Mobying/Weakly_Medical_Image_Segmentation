import matplotlib
import numpy as np

matplotlib.use('TkAgg')

from matplotlib import pylab as plt
import nibabel as nib
from nibabel import nifti1
from nibabel.viewers import OrthoSlicer3D


example_filename = 'ADNI_136_S_0429_MR_MPR-R__GradWarp__B1_Correction__N3__Scaled_Br_20070215220055664_S15534_I40387.nii'


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


img = nib.load(example_filename)
img_arr = img.get_fdata()
img_arr = flip90_right(img_arr)
img = nib.Nifti1Image(img_arr, affine=np.eye(4))
# print(img)
# print(img.header['db_name'])  # 输出头信息

width, height, queue = img.dataobj.shape
print(img.dataobj.shape)

OrthoSlicer3D(img.dataobj,title='ADNI').show()

# num = 1
# for i in range(0, queue, 10):
#     img_arr = img.dataobj[:, :, i]
#     plt.subplot(5, 4, num)
#     plt.imshow(img_arr, cmap='gray')
#     num += 1
#
#
# plt.show()