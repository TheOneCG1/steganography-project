#!/usr/bin/env python3
from PIL import Image
import numpy as np 
from tkinter import filedialog
import tkinter as tk

# Function to hide message in image
def hide_message_in_image(image_path, message):
    # Open the image
    image = Image.open(image_path)
    width, height = image.size
    img_arr = np.array(list(image.getdata()))

    if image.mode == "P":
        print("Not Supported") #Checks to see if image is in color mapped mode, The steg process is different
        return

    channels = 4 if image.mode == "RGBA" else 3

    pixels = img_arr.size // channels

    stop_indicator = "TIVH"
    stop_indicator_length = len(stop_indicator)

    message += stop_indicator #Binds stop indicator to message

    byte_message = ''.join(f"{ord(c):08b}" for c in message) #convert the message to binary represenation
    bits = len(byte_message)

    if bits > pixels:
        print("Not enough space")
    else:
        index = 0
        for i in range(pixels):
            for j in range(0,3):
                if index < bits:
                    img_arr[i][j] = int(bin(img_arr[i][j])[2:-1]+ byte_message[index],2) #Iterates loops 3 times for RGB, and hides information with LSB of the pixel values
                    index += 1
# Changes numpy array back into a image formate
    img_arr = img_arr.reshape((height, width, channels)) 
    result = Image.fromarray(img_arr.astype('uint8'), image.mode)
    result.save('encoded.png')

# Function to select file
def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename()  # Open file dialog
    return file_path

# Get the paths of the image and message
image_path = select_file()  # Select image file
message = input("Enter the message to hide: ")  # Input message to hide

# Call the function to hide message in image
hide_message_in_image(image_path, message)
