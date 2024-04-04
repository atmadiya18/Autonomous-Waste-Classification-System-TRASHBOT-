from PIL import Image
import numpy as np
import numpy as np

# open the image file using PIL
image = Image.open(r"D:\Desktop\Dataset\coffee_r\coffee_r_4.png")

pil_img = Image.open(r"D:\Desktop\Dataset\coffee_r\coffee_r_4.png")

# Resize the image to 128x128x3
resized_img = pil_img.resize((128, 128), resample=Image.ANTIALIAS)

# Save the resized image to a file
resized_img.save(r'D:\Desktop\Dataset\coffee_r\resized_image.png')

# Print the shape of the resized image
print(np.array(resized_img).shape)
