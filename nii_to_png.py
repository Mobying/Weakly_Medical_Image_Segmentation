# for i in range (4):
#     print(i)
import warnings

warnings.filterwarnings('ignore', category=FutureWarning)

import numpy as np
import os  # 遍历文件夹
import nibabel as nib  # nii格式一般都会用到这个包
import imageio  # 转换成图像
import matplotlib.image as plimg
import matplotlib.pyplot as plt

# filepath = 'ADNI'
# filepath = 'data/original/BraTS19_2013_2_1/'
filepath = 'data/preprocessed/BraTS19_2013_2_1/'
# output_path = 'PNG/original'
output_path = 'PNG/processed'
plane_list = ['x', 'y', 'z']
plane_index = 2


def nii_to_image(filepath, output_path):
    filenames = os.listdir(filepath)  # 读取nii文件夹
    slice_trans = []

    for f in filenames:
        # 开始读取nii文件
        print(f)
        img_path = os.path.join(filepath, f)
        img = nib.load(img_path)  # 读取nii
        img_fdata = img.get_fdata()
        print(img_fdata.dtype)
        print(np.min(img_fdata), np.max(img_fdata))
        img_fdata = img_fdata.T
        fname = f.replace('.nii.gz', '')  # 去掉nii的后缀名
        img_f_path = os.path.join(output_path, fname)
        # 创建nii对应的图像的文件夹
        if not os.path.exists(img_f_path):
            os.mkdir(img_f_path)  # 新建文件夹

        # 开始转换为图像
        (x, y, z) = img.shape
        # plane = img.shape(plane_index)
        for i in range(z):  # z是图像的序列
            # 你应该期待您的图像有一个shape的(y, x, 3)，这里y是垂直的像素数，x在水平方向上，并3表示三个颜色通道：红，绿，蓝。它的dtype（数据类型）应该是uint16，意思是无符号的16位整数。
            # 16位整数的范围在0到65535之间（2 ^ 16-1）。您需要将该范围强制降至8位：0 ... 255范围。

            slice = img_fdata[i, :, :]  # 选择哪个方向的切片都可以
            # slice = slice.astype(np.uint8)  #

            imageio.imwrite(os.path.join(img_f_path, '{}.png'.format(i)), slice)
            # 保存图像

        img = plimg.imread(os.path.join(img_f_path, '{}.png'.format(101)))
        # print(img.shape)
        # for j in range len(title_list)
        #     plt.title(title_list[j])
        plt.imshow(img)
        plt.axis('off')
        # plt.show()
        print(img.dtype, img.shape)
        print()


if __name__ == '__main__':
    nii_to_image(filepath, output_path)
