import tkinter as tk
from PIL import ImageTk, Image
from pathlib import Path

root = tk.Tk()
root.title("Photo Viewer")

photo_images = []
current_index = 0

def create_photo_images():
    global photo_images

    image_folder = Path("images")
    image_paths = list(image_folder.glob("*.jpg"))

    for path in image_paths:
        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)
        photo_images.append(photo)

    status_label.config(text=f"Фотография 1/{len(photo_images)}")
    show_image(0)

def show_image(idx):
    global current_image_label, photo_images, current_index

    idx = max(0, min(idx, len(photo_images) - 1))
    if idx == current_index:
        return

    current_index = idx

    current_image_label.config(image=photo_images[idx])

    status_label.config(text=f"Фотография {idx+1}/{len(photo_images)}")

    button_backward.config(state=tk.DISABLED if current_index == 0 else tk.NORMAL)
    button_forward.config(state=tk.DISABLED if current_index == len(photo_images) - 1 else tk.NORMAL)

def backward():
    global current_index
    show_image(current_index - 1)

def forward():
    global current_index
    show_image(current_index + 1)

def exit_program():
    root.quit()

button_backward = tk.Button(root, text="<<", command=backward, state=tk.DISABLED)
button_forward = tk.Button(root, text=">>", command=forward)
button_exit = tk.Button(root, text="Exit", command=exit_program)

button_backward.grid(row=1, column=0, padx=10, pady=10)
button_forward.grid(row=1, column=2, padx=10, pady=10)
button_exit.grid(row=1, column=1, padx=10, pady=10)

status_label = tk.Label(root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.E)
status_label.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E, padx=10, pady=10)

current_image_label = tk.Label(root)
current_image_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

root.bind("<Map>", lambda event: create_photo_images())

root.geometry("700x700")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()