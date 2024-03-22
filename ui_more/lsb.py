#!/usr/bin/env python3
import stepic
from PIL import Image
from cryptography.fernet import Fernet 

print(" ... Hide Away ...")

key = Fernet.generate_key()
print(key)
enc = Fernet(key)

Data = input(" Data: ")
data_enc = enc.encrypt(Data.encode())

file = input(" PHOTO: ")

img = Image.open(file)
img_stegano = stepic.encode(img, data_enc)

img_stegano.save("steggg.png")

print("*--------------*")

input(" FIN (press enter -> exit) ")