width = input("Align the table to: ")
width = int(width)

space = (width * 4) + 11

headline = "+{0:-^{space}}+".format('table of numerical systems', space=space)
row = "| {0:^{width}} | {1:^{width}} | {2:^{width}} | {3:^{width}} |".format("dec", "bin", "oct", "hex", width=width)

n = 15
rows = ""
for counter in range(0,n+1):
    d = "{0:d}".format(counter)
    b = "{0:#b}".format(counter)
    o = "{0:#o}".format(counter)
    x = "{0:#X}".format(counter)

    rows = rows + "| {d:^{width}} | {b:<{width}} | {o:<{width}} | {x:<{width}} |".format(d=d, b=b, o=o, x=x, width=width)
    if (counter < n):
        rows = rows + "\n"

hr = "+" + ('-' * space)  + "+"

print(f"{headline}\n{row}\n{hr}\n{rows}\n{hr}")