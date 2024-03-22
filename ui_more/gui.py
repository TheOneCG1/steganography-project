#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import stepic


def hide_data():
    data = data_entry.get()
    file_path = file_entry.get()
    
    try:
        img = Image.open(file_path)
        img_stegano = stepic.encode(img, data.encode('utf-8'))
        img_stegano.save("steggg.png")
        print("*--------------*")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def reveal_data():
    file_path = file_entry.get()
    
    try:
        img = Image.open(file_path)
        decoded = stepic.decode(img)
        if decoded:
            print("Decoded data:", decoded)  # Print decoded data for debugging
            output_label.config(text=decoded)
        else:
            messagebox.showinfo("Info", "No hidden data found in the image.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during decoding: {str(e)}")




def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_entry.delete(0, tk.END)
            file_entry.insert(0, file_path)
            load_image(file_path)
        else:
            messagebox.showerror("Error", "Please select a valid image file.")


def load_image(file_path):
    img = Image.open(file_path)
    img.thumbnail((200, 200))
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img


# GUI Setup
root = tk.Tk()
root.title("Image Steganography")

# Frames
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

output_frame = tk.Frame(root)
output_frame.pack(pady=10)

# Input Frame
data_label = tk.Label(input_frame, text="Data:")
data_label.grid(row=0, column=0, sticky="e")

data_entry = tk.Entry(input_frame)
data_entry.grid(row=0, column=1, padx=5, pady=5)

file_label = tk.Label(input_frame, text="Photo:")
file_label.grid(row=1, column=0, sticky="e")

file_entry = tk.Entry(input_frame)
file_entry.grid(row=1, column=1, padx=5, pady=5)

browse_button = tk.Button(input_frame, text="Browse", command=browse_file)
browse_button.grid(row=1, column=2, padx=5, pady=5)

image_label = tk.Label(input_frame)
image_label.grid(row=2, columnspan=3)

# Output Frame
hide_button = tk.Button(output_frame, text="Hide Data", command=hide_data)
hide_button.grid(row=1, column=0, padx=5, pady=5)

reveal_button = tk.Button(output_frame, text="Reveal Data", command=reveal_data)
reveal_button.grid(row=1, column=1, padx=5, pady=5)

output_label = tk.Label(output_frame)
output_label.grid(row=2, columnspan=2)

root.mainloop()
