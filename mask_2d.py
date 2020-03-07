import os

from skimage import io, data, color
import matplotlib.pyplot as plt
import numpy as np
from cv2 import imread
#
# # configuration
# config = dict()
# config['image_dir_index'] = 2
# config['dir_index'] = 0  # 0 or 1, original or processed
# config['modality_index'] = 1  # 0-4
# config['slice_number'] = 101
#
# image_dir_list = ['Sagittal_1', 'Coronal_2', 'Transverse_3']
# modalities = ['t1', 't1ce', 'flair', 't2']

image_dir = 'PNG'

image = color.rgb2gray(io.imread(image_dir + '/processed/t1ce/101.png'))
# image = imread(os.path.join(image_dir + '/processed/t1ce/101.png'))
# image = imread(os.path.join(image_dir + '/processed/t2/101.png'))
mask = imread(os.path.join(image_dir + '/processed/truth/101.png'))


def get_whole_tumor_mask(data):
    return data > 0


def get_tumor_core_mask(data):
    return np.logical_or(data == 1, data == 4)


def get_enhancing_tumor_mask(data):
    return data == 4


def draw_mask_skimage():
    # image_dir = image_dir_list[image_dir_index]  # 0-2
    # modality = modalities[modality_index]  # 0-4
    #
    # mask_overlap_path = os.path.join(image_dir + '/mask_overlap')
    # if not os.path.exists(mask_overlap_path):
    #     os.mkdir(mask_overlap_path)
    #
    # mask_original_path = os.path.join(mask_overlap_path + '/original')
    # if not os.path.exists(mask_original_path):
    #     os.mkdir(mask_original_path)
    #
    # mask_processed_path = os.path.join(mask_overlap_path + '/processed')
    # if not os.path.exists(mask_processed_path):
    #     os.mkdir(mask_processed_path)
    #
    # if dir_index == 0:
    #     # modalities += 'seg'
    #     # image_path = imread(os.path.join(image_dir + '/original/BraTS19_2013_2_1_'
    #     #                                  + modality + '/' + str(slice_number) + '.png'))
    #     # mask_path = imread(os.path.join(image_dir + '/original/BraTS19_2013_2_1_seg/'
    #     #                                 + str(slice_number) + '.png'))
    #     image_path = imread(os.path.join(image_dir + '/original/BraTS19_2013_2_1_' + modality))
    #     mask_path = imread(os.path.join(image_dir + '/original/BraTS19_2013_2_1_seg'))
    #     out_path = os.path.join(mask_original_path + '/BraTS19_2013_2_1_' + modality)
    # else:
    #     # modalities += 'truth'
    #     image_path = imread(os.path.join(image_dir + '/processed/' + modality + '/' + str(slice_number) + '.png'))
    #     mask_path = imread(os.path.join(image_dir + '/processed/truth/' + str(slice_number) + '.png'))
    #     out_path = os.path.join(mask_processed_path, modality)
    #
    # if not os.path.exists(out_path):
    #     os.mkdir(out_path)

    print(type(mask), '\n', np.max(mask), mask.dtype)
    # mask_float = 255.0 * (mask_path/255.0) ** 2
    mask_float = mask.astype(np.float64)
    print(type(mask_float), '\n', np.max(mask_float), mask_float.dtype)
    print('\nWT: ', np.sum(get_whole_tumor_mask(mask_float)),
          '\nTC: ', np.sum(get_tumor_core_mask(mask_float)),
          '\nET: ', np.sum(get_enhancing_tumor_mask(mask_float)))


    # print(slice_number)

    # print(type(image), type(mask))
    # print(image)
    # mask = data.chelsea()
    img_float = image.astype(np.float64)
    print(np.max(img_float), np.min(img_float))

    # mask_grey = color.rgb2gray(mask)
    mask_grey = 255.0 * mask / np.max(mask)
    print('mask:', np.max(mask_grey), np.min(mask_grey))
    mask_grey = color.rgb2gray(mask_grey)
    mask_grey = mask_float
    print('mask:', np.max(mask_grey), np.min(mask_grey))
    print('image:', np.max(image), np.min(image))
    print('mask_dtype:', mask_grey.dtype, 'image_dtype:', image.dtype)
    print('type:', type(mask_grey), type(image))

    ET, EDEMA, NCR_and_NET = 0, 0, 0
    print(NCR_and_NET)

    '''
    <class 'numpy.ndarray'> 
     4 uint8
    <class 'numpy.ndarray'> 
     4.0 float64
    
    WT:  6432 
    TC:  3723 
    ET:  2877
    255.0 0.0
    mask: 255.0 0.0
    mask: 4.0 0.0
    image: 255 0
    mask_dtype: float64 image_dtype: uint8
    type: <class 'numpy.ndarray'> <class 'numpy.ndarray'>
    '''

    rows, cols = mask_grey.shape
    labels = np.zeros([rows, cols])
    for i in range(rows):
        for j in range(cols):
            # if mask_grey[i, j] > 0.66:
            if mask_grey[i, j] == 1:  # ET,  labels_number:the second biggest, blue
                labels[i, j] = 2
                ET += 1
            elif mask_grey[i, j] == 0.5:  # WT-ET-TC = edema, labels_number:biggest, yellow
                labels[i, j] = 3
                EDEMA += 1
            elif mask_grey[i, j] > 0:  # TC-ET
                labels[i, j] = 1
                NCR_and_NET += 1
    # label_image = color.label2rgb(labels, bg_label=0)
    # label_image = color.label2rgb(labels, image=image)

    TC = NCR_and_NET + ET
    WT = TC + EDEMA
    print('ET: ', ET)
    print('EDEMA: ', EDEMA)
    print('NCR_and_NET: ', NCR_and_NET)
    print('TC: ', TC)
    print('WT: ', WT)

    label_image = color.label2rgb(labels, bg_label=0)
    # label_image = color.label2rgb(labels, image=image, bg_label=0)

    # figsize = mask_grey.shape[0]/ , mask_grey.shape[1]
    plt.figure(figsize=(15, 15))
    # plt.figure(figsize=(15, 15), facecolor='black')
    print(label_image.dtype)
    # plt.imshow(label_image, cmap='gray')
    plt.imshow(label_image)
    plt.axis('off')
    plt.tight_layout(pad=0)
    # plt.savefig(os.path.join(out_path + '/test_plot.png'))
    plt.savefig('test_plot.png')
    plt.show()

    # io.show()


if __name__ == '__main__':
    draw_mask_skimage()
