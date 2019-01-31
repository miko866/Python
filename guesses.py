import random

def guess():
    random_num = random.randint(0, 21)
    count = 0
    while True:
        count += 1
        number = int(input("Enter the number between 0 to 20: "))
        if number < random_num:
            print('Too small')
        elif number > random_num:
            print("Too large")
        else:
            print(f"You have got it in {count} tries.")
            break

guess()