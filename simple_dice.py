import tkinter
canvas = tkinter.Canvas(width=700, height=700)
canvas.pack()

x1 = 100
y1 = 100
x2 = 200
y2 = 200
canvas.create_oval(x1, y1, x2, y2)
canvas.create_oval(x1+(x1/2), y1, x2+(x1/2), y2)
canvas.create_oval(x2, y1, x2+x1, y2)

canvas.create_oval(x1, y1+(y1/2), x2, y2+(y1/2))

canvas.mainloop()