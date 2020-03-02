import os

import matplotlib.pyplot as plt
import numpy as np
from cv2 import imread
from skimage import color

# configuration
config = dict()
config['image_dir_index'] = 2
config['dir_index'] = 0  # 0 or 1, original or processed
config['modality_index'] = 1  # 0-4
config['slice_number'] = 101

image_dir_list = ['Sagittal_1', 'Coronal_2', 'Transverse_3']
modalities = ['t1', 't1ce', 'flair', 't2']


def draw_mask_skimage(image_dir_index=config['image_dir_index'], dir_index=config['dir_index'],
                      modality_index=config['modality_index'], slice_number=config['slice_number']):
    image_dir = image_dir_list[image_dir_index]  # 0-2
    modality = modalities[modality_index]  # 0-4
    if dir_index == 0:
        # modalities += 'seg'
        image_path = imread(os.path.join(image_dir + '/original/BraTS19_2013_2_1_'
                                         + modality + '/' + str(slice_number) + '.png'))
        mask_path = imread(os.path.join(image_dir + '/original/BraTS19_2013_2_1_seg/'
                                        + str(slice_number) + '.png'))
        out_path = os.path.join(image_dir + 'mask_overlap/original/BraTS19_2013_2_1_' + modality)
    else:
        # modalities += 'truth'
        image_path = imread(os.path.join(image_dir + '/processed/' + modality + '/' + str(slice_number) + '.png'))
        mask_path = imread(os.path.join(image_dir + '/processed/truth/' + str(slice_number) + '.png'))
        out_path = os.path.join(image_dir + 'mask_overlap/processed/' + modality)

    if not os.path.exists(out_path):
        os.mkdir(out_path)

    # image = color.rgb2gray(io.imread('PNG/processed/t1ce/101.png'))

    # image = imread(os.path.join(image_path + '/processed/t2/101.png'))
    # mask = imread(os.path.join(image_dir + '/processed/truth/101.png'))
    for i, image, mask in enumerate(image_path, mask_path):
        print(type(image), type(mask))
        # mask = data.chelsea()
        print(np.max(mask), np.min(mask))

        mask_grey = color.rgb2gray(mask)
        print('mask:', np.max(mask_grey), np.min(mask))
        print('image:', np.max(image), np.min(image))
        print('mask_dtype:', mask_grey.dtype, 'image_dtype:', image.dtype)
        print('type:', type(mask_grey), type(image))

        rows, cols = mask_grey.shape
        labels = np.zeros([rows, cols])
        for i in range(rows):
            for j in range(cols):
                # if mask_grey[i, j] > 0.66:
                if mask_grey[i, j] == 1:  # ET,  labels_number:the second biggest, blue
                    labels[i, j] = 2
                elif mask_grey[i, j] > 0.4:  # WT-ET-TC = edema, labels_number:biggest, yellow
                    labels[i, j] = 3
                elif mask_grey[i, j] > 0:  # TC-ET
                    labels[i, j] = 1
        # label_image = color.label2rgb(labels, bg_label=0)
        # label_image = color.label2rgb(labels, image=image)
        label_image = color.label2rgb(labels, image=image, bg_label=0)

        # figsize = mask_grey.shape[0]/ , mask_grey.shape[1]
        plt.figure(figsize=(15, 15))
        # plt.figure(figsize=(15, 15), facecolor='black')
        print(label_image.dtype)
        # plt.imshow(label_image, cmap='gray')
        plt.imshow(label_image)
        plt.axis('off')
        plt.tight_layout(pad=0)
        plt.savefig(os.path.join(out_path + 'test_plot.png')
        # plt.savefig('test_plot.png')
        plt.show()

        # io.show()

        if __name__ == '__main__':
            draw_mask_skimage()