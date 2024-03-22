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
data_dec = dec.decrypt(decoded.encode())

print(" Data is : " + data_dec.decode())

print("*------------------------")