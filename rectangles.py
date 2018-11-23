import tkinter
import random
canvas = tkinter.Canvas(width=640, height=480, bg="gray")
canvas.pack()
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5
def color(vzd):
    normalize = 255 - int((vzd/400)*255)
    print(vzd,normalize)
    return "#{0:02x}{0:02x}{0:02x}".format(normalize)
def create_rectangle(x, y, size, color):
    coordinates = (x-size/2, y-size/2, x+size/2, y+size/2)
    canvas.create_rectangle(coordinates, fill=color)
def draw_rectangles(count):
    for x in range(count):
        x = random.randrange(640)
        y = random.randrange(480)
        vzd = distance(x,y,320,240)
        colors = color(vzd)
        create_rectangle(x,y, vzd/6, colors)
draw_rectangles(1000)
canvas.mainloop()