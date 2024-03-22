#!/usr/bin/env python3
from PIL import Image
import numpy as np 
from tkinter import filedialog
import tkinter as tk

# Function to extract message from image
def extract_message_from_image(image_path):
    # Open the image
    image = Image.open(image_path)
    img_arr = np.array(list(image.getdata()))

    channels = 4 if image.mode == 'RGBA' else 3

    pixels = img_arr.size // channels

    secret_bits = [bin(img_arr[i][j])[-1] for i in range(pixels) for j in range(0,3)]
    secret_bits = ''.join(secret_bits)
    secret_bits = [secret_bits[i:i+8] for i in range(0, len(secret_bits),8)]

    secret_message = [chr(int(secret_bits[i],2)) for i in range(len(secret_bits))]
    secret_message = ''.join(secret_message)

    stop_indicator = "TIVH"

    if stop_indicator in secret_message:
        return secret_message[:secret_message.index(stop_indicator)]
    else:
        return "Couldn't find secret message"

# Function to select file
def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename()  # Open file dialog
    return file_path

# Get the path of the image
image_path = select_file()  # Select image file

# Call the function to extract message from image
extracted_message = extract_message_from_image(image_path)
print("Extracted message:", extracted_message)
