# for i in range (4):
#     print(i)
import warnings

warnings.filterwarnings('ignore', category=FutureWarning)

import numpy as np
import os  # 遍历文件夹
import sys

sys.path.append('.')
import nibabel as nib  # nii格式一般都会用到这个包
import imageio  # 转换成图像
import matplotlib.pyplot as plt
from cv2 import imread

# filepath = 'ADNI'
# filepath = 'mask_int16'
# filepath = 'data/original/BraTS19_2013_2_1/'
filepath = 'data/preprocessed/BraTS19_2013_2_1/'
# output_path = 'PNG/original'
# output_path = 'PNG2/original/Transverse'
# output_path = 'PNG2/original/Coronal'
# output_path = 'PNG2/original/Sagittal'
# output_path = 'PNG2/preprocessed/Transverse'
# output_path = 'PNG2/preprocessed/Coronal'
output_path = 'PNG2/preprocessed/Sagittal'
# output_path = 'PNG_int16/mask_int16'
plane_list = ['x', 'y', 'z']
plane_index = 0


# img = nib.load('data/original/BraTS19_2013_2_1/BraTS19_2013_2_1_seg.nii.gz')  # 读取nii
# img_fdata = img.get_fdata()
# print(img_fdata.dtype)


def nii_to_image(filepath, output_path):
    filenames = os.listdir(filepath)  # 读取nii文件夹
    # slice_trans = []

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    for f in filenames:
        # 开始读取nii文件
        print(f)
        img_path = os.path.join(filepath, f)
        img = nib.load(img_path)  # 读取nii
        img_fdata = img.get_fdata()
        print(img_fdata.dtype)  # float64
        print(np.min(img_fdata), np.max(img_fdata))  # 0.0 1674.0
        # img_fdata = img_as_ubyte(img_fdata)
        # print(img_fdata.dtype)  # float64
        # print(np.min(img_fdata), np.max(img_fdata))  # 0.0 1674.0

        # img_fdata = img_fdata.astype(np.uint8)
        img_fdata = img_fdata.T
        if plane_index != 2:
            img_fdata = np.flipud(img_fdata)
            # img_fdata = np.fliplr(img_fdata)

        fname = f.replace('.nii.gz', '')  # 去掉nii的后缀名
        img_f_path = os.path.join(output_path, fname)
        # 创建nii对应的图像的文件夹
        if not os.path.exists(img_f_path):
            os.mkdir(img_f_path)  # 新建文件夹

        # img_fdata = img_fdata.astype(np.float32)
        # 开始转换为图像
        (x, y, z) = img.shape
        plane = img.shape[plane_index]
        slice = img_fdata[0, :, :]
        for i in range(plane):  # z是图像的序列
            # 你应该期待您的图像有一个shape的(y, x, 3)，这里y是垂直的像素数，x在水平方向上，并3表示三个颜色通道：红，绿，蓝。它的dtype（数据类型）应该是uint16，意思是无符号的16位整数。
            # 16位整数的范围在0到65535之间（2 ^ 16-1）。您需要将该范围强制降至8位：0 ... 255范围。
            if plane_index == 2:
                slice = img_fdata[i, :, :]  # 选择哪个方向的切片都可以
            elif plane_index == 1:
                slice = img_fdata[:, i, :]  # 选择哪个方向的切片都可以
            elif plane_index == 0:
                slice = img_fdata[:, :, i]  # 选择哪个方向的切片都可以
            # print(slice.dtype)

            # print(type(slice))  # <class 'numpy.ndarray'>
            # print(slice.dtype, np.max(slice))
            # slice = float64_to_uint8(slice)

            # print(slice.dtype, np.max(slice))
            # slice2 = img_as_ubyte(slice)
            # slice = img_as_ubyte(slice)

            # print(slice1.dtype, slice2.dtype)  # float64
            # print(np.min(slice1), np.max(slice1))  # 0.0 1674.0
            # print(np.min(slice2), np.max(slice2))  # 0.0 1674.0
            imageio.imwrite(os.path.join(img_f_path, '{}.png'.format(i)), slice)
            # 保存图像

        # img = plimg.imread(os.path.join(img_f_path, '{}.png'.format(101)))
        if plane_index == 2:
            img = imread(os.path.join(img_f_path, '{}.png'.format(101)))
        elif plane_index == 1:
            img = imread(os.path.join(img_f_path, '{}.png'.format(144)))
        elif plane_index == 0:
            img = imread(os.path.join(img_f_path, '{}.png'.format(105)))


        # print(img.shape)
        # for j in range len(title_list)
        #     plt.title(title_list[j])
        # img = img.astype(np.uint8)
        # print(img.dtype, np.max(img))  # uint8 255
        # # plt.imshow(img, cmap='gray')
        plt.imshow(img)
        plt.axis('off')
        plt.show()
        print(img.dtype, img.shape)  # uint8 (240, 155, 3)
        # uint8(240, 240, 3)
        # print()


if __name__ == '__main__':
    nii_to_image(filepath, output_path)
