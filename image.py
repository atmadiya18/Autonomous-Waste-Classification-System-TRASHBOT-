from PIL import Image
import os

# Specify the image file and the directory where you want to save the copies
image_file = r"D:\Desktop\Dataset\tuna_can_r\tuna_can_r_0.png"
output_directory = r"D:\Desktop\Dataset\tuna_can_r"

pil_img = Image.open(image_file)

# Resize the image to 128x128x3
resized_img = pil_img.resize((128, 128), resample=Image.ANTIALIAS)

# Save the resized image to a file
resized_img.save(image_file)


# Open the original image
original_image = Image.open(image_file)

# Create 25 copies and save them in the output directory
for i in range(1, 26):
    copy_image = original_image.copy()
    copy_file_name = f"tuna_can_r_{i}.png"
    copy_file_path = os.path.join(output_directory, copy_file_name)
    copy_image.save(copy_file_path)

# Close the original image
original_image.close()
