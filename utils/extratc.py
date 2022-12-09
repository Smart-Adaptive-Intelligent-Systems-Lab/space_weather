import os

folder_dir = "C:\\y\\HARP_sonification\\outputs"
apples_folders_paths = [f for f in os.scandir(folder_dir) if f.is_dir() and f.name.startswith("Dawn_Active_wavelets_equal_loudness")]

import shutil

for apple_path in apples_folders_paths:
    for file in os.scandir(apple_path.path):
        if "dynamic" in file.name and not os.path.exists("C:\\y\\dataset_manager\\dataset_revolution\\images\\" + file.name):
            shutil.copyfile(file.path, "C:\\y\\dataset_manager\\dataset_revolution\\images\\\missed\\" + file.name)
