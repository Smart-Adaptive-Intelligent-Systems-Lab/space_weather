import os
import shutil

path_to_check = 'G:\\My Drive\\HARP_DATASET\\dataset_supervised\\square_images_size224_cleaned\\Ushape'
path_of_images = 'G:\\My Drive\\HARP_DATASET\\dataset_supervised\\square_images_size50_cleaned'

path_to_cut_ushape = 'G:\\My Drive\\HARP_DATASET\\dataset_supervised\\square_images_size50_cleaned\\Ushape'
path_to_cut_Noushape = 'G:\\My Drive\\HARP_DATASET\\dataset_supervised\\square_images_size50_cleaned\\NoUshape'

with os.scandir(path_of_images) as files:
    for file in files:
      if file.name.endswith('.png'):
        file_to_check_path = path_to_check + '\\' +  file.name
        if os.path.exists(file_to_check_path):
            shutil.move(file.path, path_to_cut_ushape)
        else:
            shutil.move(file.path,path_to_cut_Noushape)