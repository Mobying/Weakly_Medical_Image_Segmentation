import cv2
import matplotlib.pyplot as plt
import os
import numpy as np

# imgfile = 'image.jpg'
# pngfile = 'mask.png'

img = cv2.imread(os.path.join('PNG2/preprocessed/Transverse/t1ce/101.png'), 1)
img_original = img
mask = cv2.imread(os.path.join('PNG2/preprocessed/Transverse/truth/101.png'), 0)
# img = img_original
# img = cv2.imread(imgfile, 1)
# mask = cv2.imread(pngfile, 0)

plt.figure(figsize=(18, 6), facecolor='black')
plt.subplot(1, 3, 1)
plt.imshow(mask, cmap='gray')
# plt.imshow(img_original)
plt.axis('off')
# plt.tight_layout(pad=0)
# plt.show()
plt.subplot(1, 3, 2)
plt.imshow(img_original, cmap='gray')
plt.axis('off')

# _, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
# img = img_original
cv2.drawContours(img, contours, -1, (0, 255, 255), 2)
# cv2.drawContours(img, contours, -1, (255, 0, 0), 2, hierarchy=hierarchy, maxLevel=True)

img = img[:, :, ::-1]
img[..., 2] = np.where(mask == 1, 255, img[..., 2])

# plt.figure(figsize=(6, 6), facecolor='black')
# plt.figure(figsize=(18, 6), facecolor='black')
# plt.imshow(img)
# plt.axis('off')
# plt.tight_layout(pad=0)
# plt.show()
# plt.subplot(1, 3, 1)
# plt.imshow(mask, cmap='gray')
# # plt.imshow(img_original)
# plt.axis('off')
# # plt.tight_layout(pad=0)
# # plt.show()
# plt.subplot(1, 3, 2)
# plt.imshow(img_original, cmap='gray')
# plt.axis('off')
# plt.tight_layout(pad=0)
plt.subplot(1, 3, 3)
plt.imshow(img)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()