#!/usr/bin/env python3
from stegano import lsb
from tkinter import filedialog
import tkinter as tk

# Function to decode text from an image
def decode_text():
    # Select the encoded image file
    image_path = filedialog.askopenfilename(title="Select Encoded Image File")

    # Decode the text from the image using LSB steganography
    decoded_text = lsb.reveal(image_path)

    # Print the decoded text
    print("Decoded Text:")
    print(decoded_text)

# Function to decode file from an image
def decode_file():
    # Select the encoded image file
    image_path = filedialog.askopenfilename(title="Select Encoded Image File")

    # Decode the file from the image using LSB steganography
    decoded_file_data = lsb.reveal(image_path)

    # Prompt user to choose where to save the decoded file
    save_path = filedialog.asksaveasfilename(title="Save Decoded File As", defaultextension=".txt")

    # Convert decoded data to bytes
    decoded_bytes = decoded_file_data.encode()

    # Write the decoded file data to the chosen file
    with open(save_path, "wb") as file:
        file.write(decoded_bytes)

    print("Decoded file saved successfully!")

# Function to choose decoding method
def choose_decoding():
    print("Choose decoding method:")
    print("1. Decode Text")
    print("2. Decode File")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        decode_text()
    elif choice == "2":
        decode_file()
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run the function to choose decoding method
choose_decoding()
