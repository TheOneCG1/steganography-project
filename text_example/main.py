#!/usr/bin/env python3

# Open the file 'A-Cat.jpg' in binary append mode
# and write the bytes "Hello World" to it
with open('A-Cat.jpg', 'ab') as f:
    f.write(b"Hello World")  # Stores the bytes "Hello World" at the end of the file

# Open the file 'A-Cat.jpg' in binary read mode
with open('A-Cat.jpg', 'rb') as f:
    content = f.read()  # Read the content of the file
    offset = content.index(bytes.fromhex('FFD9'))  # Find the index of the bytes 'FFD9' (End of Image marker)
    f.seek(offset + 2)  # Move the file pointer to two bytes after the 'FFD9' marker
    print(f.read())  # Print the content of the file from the new file pointer position onwards
