#!/usr/bin/env python3
import stepic
from PIL import Image

print(" ... Hide Away ...")

Data = input("Data: ")
file = input("PHOTO: ")

img = Image.open(file)
img_stegano = stepic.encode(img, Data.encode())

img_stegano.save("somenew.jpeg")

print("*--------------*")

input("FIN (press enter -> exit) ")
