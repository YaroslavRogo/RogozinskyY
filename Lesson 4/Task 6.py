import tkinter as tk
from PIL import ImageTk, Image
from pathlib import Path

# Создаем окно root для tkinter
root = tk.Tk()
root.title("Photo Viewer")

# Создаем объекты-фотографии
photo_images = []

# Создаем функцию, которая будет вызываться после создания корневого окна
def create_photo_images():
    global photo_images

    # Создаем список путей к изображениям
    image_folder = Path("images")  # Папка с изображениями
    image_paths = list(image_folder.glob("*.jpg"))

    # Проверяем наличие изображений
    if not image_paths:
        print("В папке images нет изображений.")
        root.quit()
        return

    # Создаем объекты-фотографии
    for path in image_paths:
        try:
            image = Image.open(path)
            photo = ImageTk.PhotoImage(image)
            photo_images.append(photo)
        except Exception as e:
            print(f"Ошибка при открытии файла {path}: {str(e)}")
            continue

    # Проверяем наличие фотографий
    if not photo_images:
        print("Не удалось создать объекты-фотографии.")
        root.quit()
        return

# Функция для отображения текущей фотографии
def show_image(idx):
    global current_image_label, photo_images

    # Удостоверяемся, что индекс находится в допустимом диапазоне
    idx = max(0, min(idx, len(photo_images) - 1))

    # Обновляем отображение фотографии
    current_image_label.config(image=photo_images[idx])

    # Обновляем информацию о текущей фотографии и их общем количестве
    status_label.config(text=f"Фотография {idx + 1}/{len(photo_images)}")

    # Обновляем состояния кнопок пролистывания
    button_back.config(state=tk.NORMAL if idx > 0 else tk.DISABLED)
    button_forward.config(state=tk.NORMAL if idx < len(photo_images) - 1 else tk.DISABLED)

# Функция для пролистывания фотографий влево
def back():
    global current_index
    show_image(current_index - 1)
    current_index -= 1

# Функция для пролистывания фотографий вправо
def forward():
    global current_index
    show_image(current_index + 1)
    current_index += 1

# Функция для выхода из программы
def exit_program():
    root.quit()

# Создаем кнопки пролистывания фотографий
current_index = 0
button_back = tk.Button(root, text="<<", command=back, state=tk.DISABLED)
button_forward = tk.Button(root, text=">>", command=forward)
button_exit = tk.Button(root, text="Exit", command=exit_program)

# Пакуем кнопки с использованием grid
button_back.grid(row=1, column=0, padx=10, pady=10)
button_forward.grid(row=1, column=1, padx=10, pady=10)
button_exit.grid(row=1, column=2, padx=10, pady=10)

# Создаем информационный виджет
status_label = tk.Label(root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.E)
status_label.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E, padx=10, pady=10)

# Создаем первую фотографию (пока без изображения)
current_image_label = tk.Label(root)
current_image_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Вызываем функцию создания объектов-фотографий после создания окна root
root.bind("<Map>", lambda event: create_photo_images())

# Передаем управление tkinter
root.geometry("700x700")
root.mainloop()