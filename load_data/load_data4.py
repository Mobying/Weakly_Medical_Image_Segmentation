import sys

import SimpleITK as sitk
import matplotlib.pyplot as plt
import skimage.io as io

sys.path.append('..')


def read_img(path):
    img = sitk.ReadImage(path)
    data = sitk.GetArrayFromImage(img)
    return data


# 显示一个系列图
def show_img(data):
    for i in range(data.shape[0]):
        io.imshow(data[i, :, :], cmap='gray')
        print(i)
        io.show()


# # 单张显示
def show_img_single(ori_img):
    io.imshow(ori_img[101], cmap='gray')
    io.show()


path = '../data/original/BraTS19_2013_2_1/BraTS19_2013_2_1_seg.nii.gz'  # 数据所在路径
# mask = '../t1ce_mask.nii.gz'
# mask = '../t1ce_mask2.nii.gz'
# mask = '../t1ce_mask_float32.nii.gz'
data = read_img(mask)
# show_img(data)
img_test = data[91:111, :, :]

# 设定画图板尺寸: 与子图成比例
plt.figure(figsize=(15, 12))  # 1500 * 1200
# plt.figure()
for i in range(1, 21):
    # 1.设定子图，将每个子图输出到对应的位置
    plt.subplot(4, 5, i)  # 4 行 5列
    # 2.输出图片
    # plt.imshow(img_test[i-1], cmap='gray')
    plt.imshow(img_test[i - 1])
    # 输出图片，取出来的数据是必须处理好再输出的，此例为8 * 8
    # plt.imshow(data.reshape(8, 8))
    # 3.测试的标题和真实的标题打印出来
    plt.title('seg_' + str(i), size=16)
    # 4.关掉x y轴的刻度
    # plt.xticks([])
    # plt.yticks([])
    plt.axis('off')
    # 5.调整每隔子图之间的距离
    plt.tight_layout()

plt.show()
#
# def main():
#     a = 0
#
# if __name__ == '__main__':
#     main()
#     show_img_single(data)
