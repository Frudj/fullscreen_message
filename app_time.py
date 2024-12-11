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

def start_countdown():
    countdown(5)  # Начинаем отсчет с 5 секунд

def get_seconds_text(seconds_left):
    # Возвращаем текст с правильными окончаниями для секунд
    if seconds_left == 1:
        return "1 секунда"
    elif seconds_left in (2, 3, 4):
        return f"{seconds_left} секунды"
    else:
        return f"{seconds_left} секунд"

def countdown(seconds_left):
    if seconds_left > 0:
        close_button.config(text=f"Ознакомился(-ась) с сообщением ({get_seconds_text(seconds_left)})")
        root.after(1000, countdown, seconds_left - 1)  # через 1 секунду снова вызвать countdown
    else:
        close_button.config(text="Ознакомился(-ась) с сообщением")  # когда отсчет закончится, меняем текст кнопки
        close_button.config(state=tk.NORMAL)  # Разблокировать кнопку

# Создание главного окна
root = tk.Tk()
root.title("Сообщение от сервера")
root.attributes("-fullscreen", True)

# Чтение текста из файла
text_content = read_text_from_file()

# Создание текста в центре экрана
text_label = tk.Label(root, text=text_content, font=("Arial", 24, "bold"), wraplength=root.winfo_screenwidth(), justify="center")
text_label.pack(expand=True)

# Создание кнопки под текстом
close_button = tk.Button(root, text="Ожидайте...", font=("Arial", 24), bg="#3CB371", fg="white", command=close_program, state=tk.DISABLED)
close_button.pack(pady=20, ipadx=20, ipady=10)

# Добавление пояснительной надписи под кнопкой
info_label = tk.Label(root, text="Для закрытия данного сообщения нажмите на зелёную кнопку", font=("Arial", 10), fg="gray")
info_label.pack(pady=10)

# Добавление надписи "IT отдел" в правом верхнем углу
it_label = tk.Label(root, text="IT отдел (номер 150)", font=("Arial", 18), anchor="ne")
it_label.place(relx=1.0, rely=0.0, x=-10, y=10, anchor="ne")

# Запуск отсчета времени после загрузки окна
root.after(1000, start_countdown)  # Запускаем отсчет через 1 секунду после запуска окна

# Запуск приложения
root.mainloop()
