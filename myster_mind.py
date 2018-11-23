
import random

print("""  __  __           _            __  __ _           _
 |  \/  |         | |          |  \/  (_)         | |
 | \  / | __ _ ___| |_ ___ _ __| \  / |_ _ __   __| |
 | |\/| |/ _` / __| __/ _ \ '__| |\/| | | '_ \ / _` |
 | |  | | (_| \__ \ ||  __/ |  | |  | | | | | | (_| |
 |_|  |_|\__,_|___/\__\___|_|  |_|  |_|_|_| |_|\__,_|


""")

rulers = ("""The rules are as follows. I think the number and you'll be guessing.
If you want to finish the game, type 'END'.
At the end of the game you will see your score.""")

name = input('Enter the player name: ')
if (not name):
    name = 'player'

print('\n')
print('Ok {name}'.format(name=name))
print(rulers, end='\n\n')

correct = 0
mystake = 0

print('I guess a number...')
while True:
    ran_num = random.randint(1, 10)
    tip = (input('Your tip?: '))
    if (not tip):
        tip = '0'

    if (tip.lower().strip() == 'end'):
        row = "| {:<9} | {:>9} |"
        print('\n')
        print("+------your score------+")
        print(row.format("correctly", correct))
        print(row.format("wrong", mystake))
        print(row.format("sum", correct + mystake))
        print("+" + ("=")*23 + "+")
        break
    elif (int(tip) == ran_num):
        correct += 1
        print("Correctly!", end="\n")
    elif (int(tip) != ran_num):
        mystake += 1
        print("Wrong", end="\n")
    else:
        print("Invalid choice.")

