#!/usr/bin/env python3
#yEa
from PIL import Image
import numpy as np 

# Open the encoded image ('encoded.png')
image = Image.open('encoded.png', 'r')

# Convert the image data to a numpy array
img_arr = np.array(list(image.getdata()))

# Determine the number of color channels in the image
channels = 4 if image.mode == 'RGBA' else 3

# Calculate the total number of pixels in the image
pixels = img_arr.size // channels

# Extract the least significant bit of each pixel value
secret_bits = [bin(img_arr[i][j])[-1] for i in range(pixels) for j in range(0, 3)]

# Convert the extracted bits into a binary string
secret_bits = ''.join(secret_bits)

# Group the binary string into groups of 8 bits (bytes)
secret_bits = [secret_bits[i:i+8] for i in range(0, len(secret_bits), 8)]

# Convert each byte into a character and concatenate to form the secret message
secret_message = [chr(int(secret_bits[i], 2)) for i in range(len(secret_bits))]
secret_message = ''.join(secret_message)

# Define the stop indicator used to mark the end of the secret message
stop_indicator = "TIVH"

# Check if the stop indicator is present in the secret message
if stop_indicator in secret_message:
    # Print the secret message up to the stop indicator
    print(secret_message[:secret_message.index(stop_indicator)])
else:
    # If stop indicator is not found, print a message indicating it couldn't be found
    print("Couldn't find secret message")
