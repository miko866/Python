import tkinter
import random
import time

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()

# create gallows
def draw_gallows(x, y):
    gallows = x, y, x, y-40, x-100, y-40, x-100, y+160
    canvas.create_line(gallows, width=5)
    canvas.create_line(x-150, y+160, x-50, y+160, width=15)

# create hangman with hidden parts of body, they are created but hidden
def draw_hangman(x, y):
    head = canvas.create_oval(x-20, y, x+20, y+40, width=3, state=tkinter.HIDDEN)
    torso = canvas.create_line(x, y+40, x, y+90, width=3, state=tkinter.HIDDEN)
    larm = canvas.create_line(x-40, y+60, x, y+60, width=3, state=tkinter.HIDDEN)
    rarm = canvas.create_line(x+40, y+60, x, y+60, width=3, state=tkinter.HIDDEN)
    lleg = canvas.create_line(x, y+90, x-30, y+130, width=3, state=tkinter.HIDDEN)
    rleg = canvas.create_line(x, y+90, x+30, y+130, width=3, state=tkinter.HIDDEN)
    return head, torso, larm, rarm, lleg, rleg

def draw_letters(letters):
    start = 320 - 20 * len(letters)
    # create dictionary for letter id
    letter_ids = {letter:[] for letter in letters if letter != " "}
    for letter in letters:
        # if there is white space, skip it
        if letter == " ":
            start += 40
            continue
        canvas.create_line(start+5, 100, start+35, 100, width=2)
        idx = canvas.create_text(start+20, 85, text=letter.upper(), font="arial 30", state=tkinter.HIDDEN)

        letter_ids[letter].append(idx)
        start += 40

    return letter_ids

# load file from folder only for read
def load_wor(file_name):
    with open(file_name, "r") as fp:
        word_list = fp.read().splitlines()
    # choice random word from file
    random_word = random.choice(word_list)
    return random_word

# guess word visible text word/s
def update_letters(letter_ids, already_guessed):
    for letter, ids in letter_ids.items():
        if letter in already_guessed:
            for idx in ids:
                canvas.itemconfig(idx, state=tkinter.NORMAL)

def update_hangman(wrong_guesses, hangman_ids):
    for i in range(0, wrong_guesses):
        canvas.itemconfig(hangman_ids[i], state=tkinter.NORMAL)

# game logic
def good_guess(letter):
    already_guessed.append(letter)
    update_letters(letter_ids, already_guessed)

def bad_guess(letter):
    global wrong_guesses
    already_guessed.append(letter)
    wrong_guesses += 1
    update_hangman(wrong_guesses, hangman_ids)

def is_winner(letter_ids, already_guessed):
    for letter in letter_ids:
        if letter not in already_guessed:
            return False
    return True

def check_game_state():
    global game_state
    if is_winner(letter_ids, already_guessed):
        game_state = "WIN"
    elif wrong_guesses > 5:
        game_state = "LOSS"

def game_over(state):
    if state == "WIN":
        canvas.create_text(320, 240, text="CONGRATULATIONS", font="Arial 60", fill="RED")
    else:
        canvas.create_text(320, 240, text="GAME OVER", font="Arial 60", fill="RED")
    canvas.update()
    time.sleep(3)

# initialize global variables
draw_gallows(300, 240)
hangman_ids = draw_hangman(300, 240)
the_word = load_wor("/Users/miko866/Desktop/Python/Projects/hangman/sk_words.txt")
letter_ids = draw_letters(the_word)

game_state = "RUNNING"

already_guessed = []
wrong_guesses = 0

# main loop
while game_state == "RUNNING":
    guess = input("guess letter: ")
    if guess in already_guessed:
        continue
    elif guess in letter_ids:
        good_guess(guess)
    else:
        bad_guess(guess)

    check_game_state()
    canvas.update()

game_over(game_state)
