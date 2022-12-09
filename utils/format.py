# Import the Images module from pillow
from PIL import Image
import os

for file in os.scandir("C:\\y\\dataset_manager\\dataset_revolution\\images\\missed"):
    if file.name.endswith("png"):
        image_file = Image.open(file.path)

        new_image = image_file.resize((50,50))

        file_name = "dataset_revolution/square_images_size50/" + file.name
        new_image.save(file_name)
        print("Saved " + file_name)