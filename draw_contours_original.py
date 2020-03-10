"""功能：检测图像颜色按区块划分边框"""

import numpy as np
import cv2
import os


def detect_color(img_path, mark_img_path):
    """检测一张图片中的不同颜色区域"""
    image = cv2.imread(img_path)  # 加载图片
    # 定义颜色范围，这里可以根据自己的需求定义，注意这里颜色定义的顺序是BGR
    boundaries = [
        ([0, 0, 255], [0, 0, 255]),  # 红色
        ([0, 255, 0], [0, 255, 0]),  # 绿色
        ([255, 0, 0], [255, 0, 0])  # 蓝色
    ]

    # 遍历颜色范围
    for (lower, upper) in boundaries:
        # 由颜色范围创建NumPy数组
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # 根据特定颜色范围创建mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)

        mark_zone_with_color(output, mark_img_path, lower)


def mark_zone_with_color(src_img, mark_img, mark_color):
    """根据颜色在原始图像上标记区域"""
    # 转灰度图片
    gray = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)

    ret, binary = cv2.threshold(gray, 0, 255,
                                cv2.THRESH_BINARY)  # ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) 则只能绘制出平地轮廓

    # 轮廓检测
    _, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    newImg = cv2.imread(mark_img)
    newImg = cv2.resize(newImg, (512, 512))
    # 画图
    for i in range(len(contours) - 1):
        cv2.drawContours(image=newImg, contours=contours[i + 1], contourIdx=-1, color=tuple(mark_color.tolist()),
                         thickness=2, maxLevel=1, lineType=8)

    cv2.imwrite(mark_img, newImg)


def batch_marker(src_img_dir, draw_contours_img_dir):
    """
    批处理需要标记的图像，注意这里默认原始图像和标记了颜色区块的图像
    是同名的，但是放在不同的文件夹里。
    """
    src_imgs = get_filenames_in_dir(src_img_dir)
    dc_imgs = get_filenames_in_dir(draw_contours_img_dir)

    for src in src_imgs:
        for dc in dc_imgs:
            if src == dc:
                detect_color(os.path.join(src_img_dir, src), os.path.join(draw_contours_img_dir, dc))


def get_filenames_in_dir(dir):
    """获取一个目录下所有文件的文件名"""
    for root, dirs, files in os.walk(dir):
        return files