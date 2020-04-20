# a = 3 / 59
# print('{:.2f}'.format(a))
#
# 2.
# a = 5
# for i in range(a):
#     print(2**i * 16)
# 16
# 32
# 64
# 128
# 256

# 3.
# from keras.layers import Input
# input_shape = (4, 128, 128, 128)
# inputs = Input(input_shape)
# print(type(inputs), inputs)
# <class 'tensorflow.python.framework.ops.Tensor'>
# Tensor("input_1:0", shape=(?, 4, 128, 128, 128), dtype=float32)

#4.
# if 5e-4 == 0.0005:
#     print('True')

# 5.
# depth = 5
# for level_number in range(depth - 2, -1, -1):
#     print(level_number)

# 3 2 1 0

# 6.
n_segmentation_levels = 3
for level_number in reversed(range(n_segmentation_levels)):
    print(level_number)
# 2 1 0