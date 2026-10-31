from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

pen_color = "black"
pen_size = 5

def draw(event):
    x, y = event.x, event.y
    r = pen_size
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=pen_color, outline=pen_color)

def set_pen_size():
    global pen_size
    try:
        new_size = int(entry_size.get())
        if new_size < 1:
            mb.showwarning("Предупреждение", "Толщина должна быть больше 0")
        else:
            pen_size = new_size
    except ValueError:
        mb.showerror("Ошибка ввода", "Пожалуйста, введите целое число для толщины пера.")

def load_image():
    try:
        file_path = fd.askopenfilename(filetypes=[("PNG/GIF files", "*.png;*.gif")])
        if file_path:
            image_tk = PhotoImage(file=file_path)
            canvas.create_image(0, 0, anchor=NW, image=image_tk)
            canvas.image = image_tk
    except Exception as e:
        mb.showerror("Ошибка", f"Не удалось загрузить файл.\n"
                               f"Встроенный просмотрщик Tkinter поддерживает только PNG и GIF.\n"
                               f"Ошибка: {e}")

def save_image():
    try:
        file_path = fd.asksaveasfilename(defaultextension='*.eps', 
                                         filetypes=[('EPS files', '*.eps')])
        if file_path:
            canvas.postscript(file=file_path, colormode='color')
            mb.showinfo("Сохранено", 
                        "Изображение сохранено в формате EPS.\n"
                        "Для просмотра откройте его в графическом редакторе (например, GIMP или Inkscape).")
    except Exception as e:
        mb.showerror("Ошибка", f"Не удалось сохранить файл: {e}")

def quit_prg():
    window.destroy()

window = Tk()
window.title("Графический редактор")

canvas = Canvas(width=600, height=400)
canvas.pack()
canvas.bind("<B1-Motion>", draw)

toolbar = Frame(window)
toolbar.pack(side=BOTTOM, fill=X)

colors = ["red", "green", "blue", "black"]

for color in colors:
    lbl = Label(toolbar, bg=color, width=8, height=2)
    lbl.pack(side=LEFT)
    lbl.bind("<Button-1>", lambda e, c=color: globals().update(pen_color=c))

Label(toolbar, text="Толщина линии:").pack(side=LEFT, padx=(10, 5))
entry_size = Entry(toolbar, width=5)
entry_size.pack(side=LEFT)
entry_size.insert(0, str(pen_size))
Button(toolbar, text="Установить толщину", command=set_pen_size).pack(side=LEFT, padx=5)

menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='загрузить изображение', command=load_image)
file_menu.add_command(label='Сохранить изображение', command=save_image)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=quit_prg)

window.mainloop()