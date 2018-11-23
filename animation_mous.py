import tkinter
import random
import math
canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()
def tik():
    global angle
    angle = (angle+5) % 360
    # move
    x = cx + math.cos(math.radians(angle))*40
    y = cy + math.sin(math.radians(angle))*40
    canvas.coords(oval_id, x-20, y-20, x+20, y+20)
    canvas.after(1, tik)
def tok():
    color = "#{:06x}".format(random.randrange(256**3))
    canvas.itemconfig(oval_id, fill=color)
    canvas.after(500, tok)
def mouse_move(event):
    global cx,cy
    cx = event.x
    cy = event.y
canvas.bind("<Motion>", mouse_move)
cx = 320
cy = 240
oval_id = canvas.create_oval(cx-20, cy-20, cx+20, cy+20)
angle = 0
tik()
tok()
canvas.mainloop()