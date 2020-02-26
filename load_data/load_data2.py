import SimpleITK as sitk
import numpy as np
case_path = './data/flair.nii.gz'
# 1.读取DICOM序列
reader = sitk.ImageSeriesReader()
dicom_names = reader.GetGDCMSeriesFileNames(case_path)
reader.SetFileNames(dicom_names)
image = reader.Execute()
image_array = sitk.GetArrayFromImage(image) # z, y, x
origin = image.GetOrigin() # x, y, z
spacing = image.GetSpacing() # x, y, z

# # 2.读取单张：
# image = sitk.ReadImage(slice_path)
# image_array = sitk.GetArrayFromImage(image) # z, y, x
#
# # 3.读取mhd文件:
# image = sitk.ReadImage(mhd_path)
# image_array = sitk.GetArrayFromImage(image) # z, y, x
# origin = image.GetOrigin() # x, y, z
#
# # 4.插值:
# reader = sitk.ImageSeriesReader()
# dicom_names = reader.GetGDCMSeriesFileNames(case_path)
# reader.SetFileNames(dicom_names)
# image = reader.Execute()
# resample = sitk.ResampleImageFilter()
# resample.SetOutputDirection(image.GetDirection())
# resample.SetOutputOrigin(image.GetOrigin())
# newspacing = [1, 1, 1]
# resample.SetOutputSpacing(newspacing)
# newimage = resample.Execute(image)
