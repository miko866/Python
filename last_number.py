# this script will give last num 

def last_num(n):
    n = str(n)
    return int(n[len(n) - 1])

print(last_num(int(input("Enter number: "))))
