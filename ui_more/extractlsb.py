#!/usr/bin/env python3
import stepic
from PIL import Image

print("*----------------------------")



file = input(" PHOTO: ")

img = Image.open(file)
decoded = stepic.decode(img)

print(" Data is : " + decoded)

print("*------------------------")
