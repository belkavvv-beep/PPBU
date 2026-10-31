import tkinter as tk
win = tk.Tk()
win.title('Калькулятор')
win.geometry('370x215')

msg = tk.Label(win, text='Введите три числа и нажмите на кнопку для вычисления суммы', font=('Arial', 8))
msg.pack(pady=12)

num1 = tk.Entry(win)
num1.pack(pady=1)

num2 = tk.Entry(win)
num2.pack(pady=1)

num3 = tk.Entry(win)
num3.pack(pady=1)

def add():
    x = int(num1.get())
    y = int(num2.get())
    z = int(num3.get())
    res = x + y + z
    msg.config(text=f"Результат: {res}")

def multiply():
    x = int(num1.get())
    y = int(num2.get())
    z = int(num3.get())
    res = x * y * z
    msg.config(text=f"Результат: {res}")

btn = tk.Button(win, text='Сложить три числа', command=add)
btn.pack(pady=1)

btn = tk.Button(win, text='Умножить три числа', command=multiply)
btn.pack(pady=1)

msg = tk.Label(win, text='', font=('Arial', 15))
msg.pack(pady=5)

win.mainloop()
