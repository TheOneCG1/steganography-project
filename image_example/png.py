#!/usr/bin/env python3

from PIL import Image
import io

""" 
img = Image.open('dripgoku.png')
byte_arr = io.BytesIO()
img.save(byte_arr, format='PNG')

CONVERTS THE IMAGE
"""

# Open the file 'mountain.jpeg' in binary read mode
with open('mountain.jpeg', 'rb') as f:
    content = f.read()  # Read the content of the file
    offset = content.index(bytes.fromhex('FFD9'))  # Find the index of the bytes 'FFD9' (End of Image marker)
    f.seek(offset + 2)  # Move the file pointer to two bytes after the 'FFD9' marker

    # "DECRYPTS"
    # Read the content of the file from the new file pointer position onwards
    new_img = Image.open(io.BytesIO(f.read()))  # Open the image using Pillow
    new_img.save("new_image.png")  # Save the image as 'new_image.png'
