#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import os


# ## Step-by-Step Solution
# 1. Reading the image. (Do you need to know about libraries, be mature man).
# 2. Giving the number of rows and columns if image is like the sample one.
# 3. calculating each images height by dividing it in total number of rows and columns as mentioned.
# 4. Creating folder to save output images.
# 5. Lastly, cutting all the pieces or dividing images into total pieces as per number of rows and columns mentioned.
# 6. Hurray, Work done!

# In[2]:


image_path = "bars_original.jpg"  
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image. Check the file path.")
    exit()

num_rows = 6 
num_cols = 3 


image_height, image_width, _ = image.shape
sub_image_height = image_height // num_rows
sub_image_width = image_width // num_cols

output_dir = "output_bars"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for row in range(num_rows):
    for col in range(num_cols):
        start_x = col * sub_image_width
        start_y = row * sub_image_height
        end_x = (col + 1) * sub_image_width
        end_y = (row + 1) * sub_image_height
        
        sub_image = image[start_y:end_y, start_x:end_x]
        output_path = os.path.join(output_dir, f"piece_{row}_{col}.jpg")
        cv2.imwrite(output_path, sub_image)
        print(f"Saved: {output_path}")

print("Image successfully split into pieces!")


# In[ ]:




