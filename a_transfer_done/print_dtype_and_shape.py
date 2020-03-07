import SimpleITK as sitk

img = '../data/original/BraTS19_2013_2_1/BraTS19_2013_2_1_t1ce.nii.gz'
img2 = '../data/preprocessed/BraTS19_2013_2_1/t1ce.nii.gz'
img3 = '../data/predict/BraTS19_2013_2_1/data_t1ce.nii.gz'
# mask = 't1ce_mask.nii.gz'
# mask = 't1ce_mask2.nii.gz'
mask = 't1ce_mask_float32.nii.gz'

img = sitk.ReadImage(img)
img_arr = sitk.GetArrayFromImage(img)
img2 = sitk.ReadImage(img2)
img2_arr = sitk.GetArrayFromImage(img2)
img3 = sitk.ReadImage(img3)
img3_arr = sitk.GetArrayFromImage(img3)
mask = sitk.ReadImage(mask)
mask_arr = sitk.GetArrayFromImage(mask)
print('original img:', img_arr.dtype, img_arr.shape)
print('\nprocessed img:', img2_arr.dtype, img2_arr.shape)
print('\npredict img:', img3_arr.dtype, img3_arr.shape)
print('\nmask:', mask_arr.dtype, mask_arr.shape)
# print(img.dataobj.shape, mask.dataobj.shape)

'''
original img: int16 (155, 240, 240)
processed img: float32 (155, 240, 240)
predict img: float32 (128, 128, 128)
mask: uint8 (155, 240, 240, 3)

'''