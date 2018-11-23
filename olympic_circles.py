
import tkinter
canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()

radius = input("Set a radius: ")
radius_int = int(radius)
radius = radius_int
cordinator = input("Enter the first (one) coordinator: ")
cordinator_int = int(cordinator)
cordinator = cordinator_int

first = cordinator
second = cordinator + radius
colors = ["blue", "yellow", "black","green", "red"]
cordinator = cordinator - radius

loop = 1
for color in colors:
    cordinator = cordinator + radius + (radius*0.02)
    if(loop % 2 != 0):
        direct = first
    else:
        direct = second

    canvas.create_oval(cordinator, direct, cordinator + (radius * 2), direct + (radius * 2), outline=color)
    loop = loop + 1

    

canvas.mainloop()
