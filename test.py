# # import tensorflow as tf
# # a = tf.constant([1.,2.,3.,4.,5.,6.], shape=[2,3], name='a')
# # b = tf.constant([1.,2.,3.,4.,5.,6.], shape=[3,2], name='b')
# # c = tf.matmul(a,b)
# #
# # with tf.Session(config= tf.ConfigProto(log_device_placement=True)) as sess:
# #     print(sess.run(c))
# #
# # from __future__ import print_function
# # %matplotlib inline
# import matplotlib.pyplot as plt
# from ipywidgets import interact, FloatSlider
# import SimpleITK as sitk
# from load_data4 import show_img
# # from myshow import myshow, myshow3d
# img_T1 = "data/original/BraTS19_2013_2_1/BraTS19_2013_2_1_t1.nii.gz"
# seg = "data/original/BraTS19_2013_2_1/BraTS19_2013_2_1_seg.nii.gz"
# img_T1 = sitk.ReadImage(img_T1)
# # To visualize the labels image in RGB with needs a image with 0-255 range
# img_T1_255 = sitk.Cast(sitk.RescaleIntensity(img_T1), sitk.sitkUInt8)
# print(img_T1_255,type(img_T1_255))
# # show_img(img_T1)
# seg = sitk.ReadImage(seg)
# test = sitk.LabelOverlay(img_T1_255, seg)
# test = sitk.GetArrayFromImage(test)
# print(type(test))
#
# def main():
#     show_img(test)
# # show_img(test)
# # show_img(sitk.LabelOverlay(img_T1_255, seg), "Brain tumor label")
# if __name__ == '__main__':
#     main()
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from nibabel.viewers import OrthoSlicer3D
import nibabel as nib
import skimage.io as io
import numpy as np


def fz(arr):
    return arr[::-1]


def flip_ud(arr):
    return np.flipud(arr)


def flip_lr(arr):
    return np.fliplr(arr)


# img = nib.load('data/preprocessed/BraTS19_2013_2_1/t1ce.nii.gz')
img = nib.load('data/original/BraTS19_2013_2_1/BraTS19_2013_2_1_t1ce.nii.gz')
# img = nib.load('data/original/BraTS19_2013_2_1/BraTS19_2013_2_1_t1.nii.gz')
# img = nib.load('data/original/BraTS19_2013_2_1/BraTS19_2013_2_1_flair.nii.gz')
img_arr = img.get_data()
img_arr = flip_lr(img_arr) # 左右翻转
print(img_arr.shape)
img = nib.Nifti1Image(img_arr, affine=None)
# img_arr = np.squeeze(img_arr)
# io.imshow(img_arr[101,:,:])
# print(img.dataobj.shape, type(img.slicer[91:]), type(img.slicer[91:].dataobj))
# OrthoSlicer3D(img.slicer[91:,1:,1:].dataobj).show()
# ax.axes.get_yaxis().set_visible(False)
# ax.axes.get_xaxis().set_visible(False)
plot = OrthoSlicer3D(img.dataobj, axes=None, title='t1ce_2')
# plot.show()
# OrthoSlicer3D(img.dataobj, axes=None, title='t1ce').show()
# print(
plot.set_position(113, 133, 101)
# plot._set_volume_index(0, update_slices=True)
# plot.draw()
# print(plot.n_volumes)
# plot._plt.title('try')
# plot
plot._plt.savefig('test')
plot.show()
# plot.__annotations__

# width,height,queue=img.dataobj.shape

# num = 1
# for i in range(0,queue,10):
#
#     img_arr = img.dataobj[:,:,i].T
#     plt.subplot(5,4,num)
#     plt.imshow(img_arr,cmap='gray')
#     num +=1
#
#
# plt.show()