print("""
#     _____ _          _     _                    _______            
#    / ____| |        (_)   | |                  |__   __|           
#   | |    | |__  _ __ _ ___| |_ _ __ ___   __ _ ___| |_ __ ___  ___ 
#   | |    | '_ \| '__| / __| __| '_ ` _ \ / _` / __| | '__/ _ \/ _ \ 
#   | |____| | | | |  | \__ \ |_| | | | | | (_| \__ \ | | |  __/  __/
#    \_____|_| |_|_|  |_|___/\__|_| |_| |_|\__,_|___/_|_|  \___|\___|
#                                                                    
#                                                                    
""")


def pattern():
    a = int(input("Enter the number of rows: "))
    b = a - 3
    for k in range(b, 0, -1):
        for f in range(0, 5):
            print(" ", end=" ")
        for j in range(0, k):
            print(" ", end=" ")
        for h in range(0, 2 * (b - k) + 1):
            print("*", end=" ")
        print("\r")

    c = a - 2
    for k in range(c, 0, -1):
        for f in range(0, 3):
            print(" ", end=" ")
        for j in range(0, k):
            print(" ", end=" ")
        for h in range(0, (2 * (c - k) + 1) + 2):
            print("*", end=" ")
        print("\r")

    d = a - 1
    for k in range(d, 0, -1):
        for f in range(0, 2):
            print(" ", end=" ")
        for j in range(0, k):
            print(" ", end=" ")
        for h in range(0, (2 * (d - k) + 1) + 2):
            print("*", end=" ")
        print("\r")

    e = a - 0
    for k in range(e, 0, -1):
        for j in range(0, k):
            print(" ", end=" ")
        for h in range(0, ( 2 * (e - k) + 1) + 4):
            print("*", end=" ")
        print("\r")

    for k in range(0, a):
        for j in range(0, a + 1):
            print(" ", end=" ")
        for h in range(0, 3):
            print("*", end=" ")
        print("\r")


pattern()
