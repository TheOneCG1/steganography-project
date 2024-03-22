#!/usr/bin/env python3
import stepic
from PIL import Image
from cryptography.fernet import Fernet

print("*----------------------------")

key = input(" KEY: ")
dec = Fernet(key)

file = input(" PHOTO: ")

img = Image.open(file)
decoded = stepic.decode(img)

# Here, we're directly decrypting the decoded data without encoding it back to bytes.
data_dec = dec.decrypt(decoded)

# Write the decrypted data to a file
with open("extracted_image.png", "wb") as f:
    f.write(data_dec)

print("Image extracted successfully and saved as 'extracted_image.png'.")

print("*------------------------")
