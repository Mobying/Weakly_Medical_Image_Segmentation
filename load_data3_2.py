import SimpleITK as sitk
import matplotlib.pyplot as plt
import numpy as np
import os
import nibabel as nib

NII_DIR = './data'  # nii文件所在root目录


def read_nii_file2(img_path):
    '''
    根据nii文件路径读取nii图像
    '''
    nii_image = sitk.ReadImage(img_path)
    return nii_image


def nii_one_slice2(image):
    '''
    显示nii image中的其中1张slice
    '''
    # C,H,W
    # SimpleITK读出的image的data的数组顺序为：Channel,Height，Width
    image_arr = sitk.GetArrayFromImage(image)
    print(type(image_arr))
    print(image_arr.shape)
    image_2d = image_arr[85, :, :]
    plt.imshow(image_2d, cmap='gray')
    plt.show()


nii_image2 = read_nii_file2(os.path.join(NII_DIR, 'BraTS19_2013_2_1', 'BraTS19_2013_2_1_flair.nii.gz'))
nii_one_slice2(nii_image2)
