import random

print("\n")
print("It's a year of 1500 and you live in a cottage. \nTry to survive. :-)")

# menu
def menu():
    print("What do you do?")
    print("(1) Cut down a tree.")
    print("(2) Cut the timbers on the logs.")
    print("(3) Go sleep.")
    print("(4) End simulation.")

def message():
    if timbers > 1:
        print("Is day {0}. In the hovel have you {1} timbers and {2} logs.".format(
            days, timbers, logs))
    else:
        print("Is day {0}. In the hovel have you {1} timber and {2} log.".format(
            days, timbers, logs))

    print("_ " * 30)
    print("\n")

def count():
    global logs
    if logs > 0:
        print("Prešiel deň a splali si jendo poleno.")
        logs -= 1
    else:
        print("You have no more logs and your freezen.")

# definition of variables
days = 1
timbers = 0
logs = 3
threes = 0
start = True

while start:

    message()
    print("\n")

    menu()

    choice = int(input("Enter your choice: "))
    print("\n")
    if choice == 1:
        falled_threes = random.randrange(1, 4)
        falled_timbers = random.randrange(2, 5)
        print("You went to the wood and cut off {0} threes and you have {1} timbers.".format(falled_threes, falled_timbers))

        threes += falled_threes
        timbers += falled_timbers
    elif choice == 2:
        if timbers > 0:
            cut_timbers = timbers
            cut_timbers = random.randrange(2, 5)
            if cut_timbers > timbers:
                old_timbers = timbers * 2
                print("You cut off {0} timbers on {1} logs".format(timbers, old_timbers))
                logs += old_timbers
                timbers = 0
            else:
                timbers -=cut_timbers
                cut_logs = cut_timbers * 2
                print("You cut off {0} timbers on {1} logs".format(cut_timbers, cut_logs))

                logs += cut_logs
        else:
            print("You have no timbers.")
    elif choice == 3:
        print("Go sleep... chrrr... chrrr...")
    elif choice == 4:
        print("Your are death.")
        break
    else:
        print("Neplatný vstup.")

    count()

    days += 1


