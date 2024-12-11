import tkinter as tk
from tkinter import messagebox
import os

def close_program():
    root.destroy()

def read_text_from_file():
    file_path = "C:\\VHOST\\text.txt"  # Полный путь к файлу
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    else:
        return f"Файл {file_path} не найден."

# Создание главного окна
root = tk.Tk()
root.title("Сообщение")
root.attributes("-fullscreen", True)

# Чтение текста из файла
text_content = read_text_from_file()

# Создание текста в центре экрана
text_label = tk.Label(root, text=text_content, font=("Arial", 24), wraplength=root.winfo_screenwidth(), justify="center")
text_label.pack(expand=True)

# Создание кнопки под текстом
close_button = tk.Button(root, text="Ознакомился(-ась) с сообщением", font=("Arial", 24), bg="blue", fg="white", command=close_program)
close_button.pack(pady=20, ipadx=20, ipady=10)

# Добавление пояснительной надписи под кнопкой
info_label = tk.Label(root, text="Для закрытия данного уведомления нажмите на синюю кнопку", font=("Arial", 10), fg="gray")
info_label.pack(pady=10)

# Добавление надписи "IT отдел" в правом верхнем углу
it_label = tk.Label(root, text="IT отдел (номер 150)", font=("Arial", 30), anchor="ne")
it_label.place(relx=1.0, rely=0.0, x=-10, y=10, anchor="ne")

# Запуск приложения
root.mainloop()
