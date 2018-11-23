# graphic dice

import tkinter
import random

canvas_width = 640
canvas_height = 480
canvas = tkinter.Canvas(width=canvas_width, height=canvas_height)
canvas.pack()

number = random.randint(1,6)

print("There was a number on the cube {}".format(number))
print("I draw a dice...")

size = 200

# center of dice
x, y = canvas_width / 2, canvas_height / 2
unit = size / 5
radius = size*0.03

# use polygon for the outline of the dice and the radius we use to calculate the decoupling
#
#    p2___p3
# p1/       \p4
#   |       |
#   |       |
# p8\_______/p5
#   p7    p6
#
 
p1 = x - size / 2,  y-size / 2 + radius
p2 = x - size / 2 + radius, y - size / 2
p3 = x + size / 2 - radius, y - size / 2
p4 = x + size / 2,  y-size / 2 + radius
p5 = x + size / 2,  y+size / 2 - radius
p6 = x + size / 2 - radius, y + size / 2
p7 = x - size / 2 + radius, y + size / 2
p8 = x - size / 2,  y+size / 2 - radius

canvas.create_polygon(p1, p2, p3, p4, p5, p6, p7, p8,
                      outline="black", fill="gray", width=3)

# Here we calculate all the coordinates of the dots forward.
#
#        a a a
#        1 2 3
#      +-------+
#   b1 | 1   2 |
#   b2 | 3 4 5 |
#   b3 | 6   7 |
#      +-------+
#

a1 = x - 1.5*unit
a2 = x
a3 = x + 1.5*unit

b1 = y - 1.5*unit
b2 = y
b3 = y + 1.5*unit

x1, y1 = a1, b1
x2, y2 = a3, b1
x3, y3 = a1, b2
x4, y4 = a2, b2
x5, y5 = a3, b2
x6, y6 = a1, b3
x7, y7 = a3, b3

# Drawing of dots!

if (number == 1 or number == 3 or number == 5):
    canvas.create_oval(a2 - (unit / 2), b2 - (unit / 2), (a2 - (unit / 2)) + unit, (b2 - (unit / 2)) + unit)

if (number >= 2 and number <= 6):
    canvas.create_oval(a3 - (unit / 2), b3 - (unit / 2), (a3 - (unit / 2)) + unit, (b3 - (unit / 2)) + unit)
    canvas.create_oval(a1 - (unit / 2), b1 - (unit / 2), (a1 - (unit / 2)) + unit, (b1 - (unit / 2)) + unit)

if (number >= 4 and number <= 6):
    canvas.create_oval(a3 - (unit / 2), b1 - (unit / 2), (a3 - (unit / 2)) + unit, (b1 - (unit / 2)) + unit)
    canvas.create_oval(a1 - (unit / 2), b3 - (unit / 2), (a1 - (unit / 2)) + unit, (b3 - (unit / 2)) + unit)

if (number == 6):
    canvas.create_oval(a1 - (unit / 2), b2 - (unit / 2), (a1 - (unit / 2)) + unit, (b2 - (unit / 2)) + unit)
    canvas.create_oval(a3 - (unit / 2), b2 - (unit / 2), (a3 - (unit / 2)) + unit, (b2 - (unit / 2)) + unit)


canvas.mainloop()

