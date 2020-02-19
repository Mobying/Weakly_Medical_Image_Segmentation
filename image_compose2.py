import PIL.Image as Image
from PIL import Image
import SimpleITK as sitk
import numpy as np
import os


def read_img(path):
    img = sitk.ReadImage(path)
    data = sitk.GetArrayFromImage(img)
    return data


path = './data/BraTS19_2013_2_1/BraTS19_2013_2_1_flair.nii.gz'  # 数据所在路径
data = read_img(path)
img_set = data[91:111, :, :]
basemat = np.atleast_2d(img_set)

# IMAGES_FORMAT = ['.jpg', '.JPG']  # 图片格式
IMAGE_SIZE = 32  # 每张小图片的大小
IMAGE_ROW = 4  # 图片间隔，也就是合并成一张图后，一共有几行
IMAGE_COLUMN = 5  # 图片间隔，也就是合并成一张图后，一共有几列
IMAGE_SAVE_PATH = 'final.jpg'  # 图片转换后的地址


# 定义图像拼接函数
def image_compose2():
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE))  # 创建一个新图
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = img_set[IMAGE_COLUMN * (y - 1) + x - 1].resize(
                IMAGE_SIZE, Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE, (y - 1) * IMAGE_SIZE))
    return to_image.save(IMAGE_SAVE_PATH)  # 保存新图


image_compose2()  # 调用函数
