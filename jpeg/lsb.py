#!/usr/bin/env python3
from stegano import lsb
from tkinter import filedialog
import tkinter as tk

# Function to encode text data into an image
def encode_text():
    # Select an image file
    image_path = filedialog.askopenfilename(title="Select Image File")

    # Prompt user for the text to encode
    text_to_encode = input("Enter the text to encode: ")

    # Encode the text into the image using LSB steganography
    secret_image = lsb.hide(image_path, text_to_encode)

    # Save the encoded image
    secret_image.save("encoded_image.png")
    print("Text encoded successfully!")

# Function to encode file data into an image
def encode_file():
    # Select an image file
    image_path = filedialog.askopenfilename(title="Select Image File")

    # Prompt user to select the file to encode
    file_path = filedialog.askopenfilename(title="Select File to Encode")

    # Read the file data
    with open(file_path, "rb") as file:
        file_data = file.read()

    # Encode the file data into the image using LSB steganography
    secret_image = lsb.hide(image_path, file_data)

    # Save the encoded image
    secret_image.save("encoded_image.png")
    print("File encoded successfully!")

# Function to choose encoding method
def choose_encoding():
    print("Choose encoding method:")
    print("1. Encode Text")
    print("2. Encode File")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        encode_text()
    elif choice == "2":
        encode_file()
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run the function to choose encoding method
choose_encoding()
