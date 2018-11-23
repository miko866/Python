import tkinter
canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()
def draw():
    global coordinates
    coordinates += [x, y]
    canvas.coords(line_id, coordinates)
def left(event):
    global x
    x -= 10
    draw()
def right(event):
    global x
    x += 10
    draw()
def up(event):
    global y
    y -= 10
    draw()
def down(event):
    global y
    y += 10
    draw()
x, y = 100,100
coordinates = [x, y]
line_id = canvas.create_line(0, 0, 0, 0)
canvas.bind_all('<Left>', left)
canvas.bind_all('<Right>', right)
canvas.bind_all('<Up>', up)
canvas.bind_all('<Down>', down)
canvas.mainloop()