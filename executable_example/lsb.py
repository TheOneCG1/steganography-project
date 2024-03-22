#!/usr/bin/env python3

from PIL import Image
import numpy as np 

# Define the message to hide in the image
message_to_hide = "This is my secret message!"

# Open the image 'dripgokuV2.png'
image = Image.open('dripgokuV2.png', 'r')

# Get the dimensions of the image
width, height = image.size

# Convert the image data to a numpy array
img_arr = np.array(list(image.getdata()))

# Check if the image mode is supported
if image.mode == "P":
    print("Not Supported")
    exit()

# Determine the number of color channels in the image
channels = 4 if image.mode == "RGBA" else 3

# Calculate the total number of pixels in the image
pixels = img_arr.size // channels

# Define a stop indicator to mark the end of the message
stop_indicator = "TIVH"
stop_indicator_length = len(stop_indicator)

# Append the stop indicator to the message
message_to_hide += stop_indicator

# Convert the message to binary representation
byte_message = ''.join(f"{ord(c):08b}" for c in message_to_hide)
