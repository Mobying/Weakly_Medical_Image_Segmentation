import matplotlib.pyplot as plt
import numpy as np
import os

# path1 = os.path.abspath('.')
# NII_DIR = path1 + '/data'  # nii文件所在root目录
NII_DIR = './data'  # nii文件所在root目录

import nibabel as nib


def read_nii_file1(nii_path):
    '''
    根据nii文件路径读取nii图像
    '''
    nii_image = nib.load(nii_path)
    return nii_image


def nii_one_slice1(image):
    '''
    显示nii image中的其中1张slice
    '''
    image_arr = image.get_data()
    print(type(image_arr))
    print(image_arr.shape)
    # 注意：nibabel读出的image的data的数组顺序为：Width，Height，Channel
    # 将2d数组转置，让plt正常显示
    image_2d = image_arr[:, :, 85].transpose((1, 0))
    plt.imshow(image_2d, cmap='gray')
    plt.show()


nii_image1 = read_nii_file1(os.path.join(NII_DIR, 'BraTS19_2013_2_1', 'BraTS19_2013_2_1_flair.nii.gz'))
nii_one_slice1(nii_image1)