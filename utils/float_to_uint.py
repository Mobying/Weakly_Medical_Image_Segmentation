import numpy as np


def float64_to_uint8(data):
    info = np.iinfo(data.dtype)  # 获取传入图像类型的信息
    data = data.astype(np.float64) / info.max  # 将数据规划化为0-1
    data = 255 * data  # 缩放255
    img = data.astype(np.unit8)
    return img

# def uint8_to_float64(data):
#     info = np.iinfo(data.dtype)  # 获取传入图像类型的信息
#     data = data.astype(np.float64) / info.max  # 将数据规划化为0-1
#     data = 255 * data  # 缩放255
#     img = data.astype(np.unit8)
#     return img
