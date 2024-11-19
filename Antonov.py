import tkinter as tk
from tkinter import messagebox

def check_triangle():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())

        if a <= 0 or b <= 0 or c <= 0:
            messagebox.showerror("Ошибка", "Стороны должны быть положительными целыми числами.")
            return

        if a + b <= c or a + c <= b or b + c <= a:
            messagebox.showerror("Ошибка", "С указанными сторонами треугольник не может существовать.")
            return

        triangle_type = ""
        sides = sorted([a, b, c])
        a, b, c = sides

        if a == b == c:
            triangle_type = "равносторонний"
        elif a == b or b == c or a == c:
            triangle_type = "равнобедренный"
        else:
            triangle_type = "разносторонний"


        if a**2 + b**2 == c**2:
            triangle_type += " и прямоугольный"

        elif a**2 + b**2 < c**2:
            triangle_type += " и тупоугольный"

        else:
            triangle_type += " и остроугольный"

        messagebox.showinfo("Результат", f"Треугольник является {triangle_type}.")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целые числа.")

root = tk.Tk()
root.title("Определение типа треугольника")
root.geometry("300x300")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, bg="#ffffff", padx=10, pady=10)
frame.pack(padx=20, pady=20)

label_title = tk.Label(frame, text="Введите стороны треугольника", font=("Arial", 14), bg="#ffffff")
label_title.pack(pady=10)

label_a = tk.Label(frame, text="Сторона A:", font=("Arial", 12), bg="#ffffff")
label_a.pack(anchor='w')
entry_a = tk.Entry(frame, font=("Arial", 12))
entry_a.pack(pady=5)

label_b = tk.Label(frame, text="Сторона B:", font=("Arial", 12), bg="#ffffff")
label_b.pack(anchor='w')
entry_b = tk.Entry(frame, font=("Arial", 12))
entry_b.pack(pady=5)

label_c = tk.Label(frame, text="Сторона C:", font=("Arial", 12), bg="#ffffff")
label_c.pack(anchor='w')
entry_c = tk.Entry(frame, font=("Arial", 12))
entry_c.pack(pady=5)

check_button = tk.Button(root, text="Проверить", command=check_triangle, font=("Arial", 12), bg="#4CAF50", fg="white")
check_button.pack(pady=10)

root.mainloop()