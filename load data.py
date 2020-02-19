import SimpleITK as sitk
from matplotlib import pyplot as plt


def showNii(img):
    for i in range(img.shape[0]):
        plt.imshow(img[i, :, :], cmap='gray')
        plt.show()


# itk_img = sitk.ReadImage('BraTS19_2013_2_1_flair.nii')
# img = sitk.GetArrayFromImage(itk_img)
# showNii(img)
#
# itk_img = sitk.ReadImage('BraTS19_2013_2_1_t1.nii')
# img = sitk.GetArrayFromImage(itk_img)
# showNii(img)
#
# itk_img = sitk.ReadImage('BraTS19_2013_2_1_t1ce.nii')
# img = sitk.GetArrayFromImage(itk_img)
# showNii(img)
# #
# itk_img = sitk.ReadImage('BraTS19_2013_2_1_t2.nii')
# img = sitk.GetArrayFromImage(itk_img)
# showNii(img)
#
itk_img = sitk.ReadImage('t2.nii.gz')
img = sitk.GetArrayFromImage(itk_img)
showNii(img)
