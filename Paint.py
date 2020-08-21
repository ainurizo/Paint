from tkinter import *

frame_width = 700
frame_height = 500
brush_size = 3
brush_color = "black"


def paint(event):
    global brush_size
    global brush_color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size

    frame.create_oval(x1, y1, x2, y2, fill=brush_color, outline=brush_color)


def change_brush_size(new_size):
    global brush_size
    brush_size = new_size


def change_brush_color(new_color):
    global brush_color
    brush_color = new_color


root = Tk()
root.title("Paint")

frame = Canvas(root,
               width=frame_width,
               height=frame_height,
               bg="white")

red_button = Button(text="Красный", width=10, command=lambda: change_brush_color("red"))
yellow_button = Button(text="Желтый", width=10, command=lambda: change_brush_color("yellow"))
blue_button = Button(text="Синий", width=10, command=lambda: change_brush_color("blue"))
black_button = Button(text="Черный", width=10, command=lambda: change_brush_color("black"))
remove_button = Button(text="Ластик", width=10, command=lambda: change_brush_color("white"))
clear_button = Button(text="Удалить все", width=10, command=lambda: frame.delete("all"))

size_btn_5 = Button(text="5", width=10, command=lambda: change_brush_size(5))
size_btn_3 = Button(text="3", width=10, command=lambda: change_brush_size(3))






frame.bind("<B1-Motion>", paint)

frame.grid(column=0, row=0, columnspan=7, padx=5, pady=5, sticky=E + W + S + N)
frame.columnconfigure(2, weight=1)
frame.rowconfigure(6, weight=1)

red_button.grid(column=0, row=2)
yellow_button.grid(column=1, row=2)
black_button.grid(column=2, row=2)
blue_button.grid(column=3, row=2)
remove_button.grid(column=4, row=2)
clear_button.grid(column=5, row=2)
size_btn_3.grid(column=0,row=3)
size_btn_5.grid(column=1,row=3)


root.mainloop()
