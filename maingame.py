# made by Shreyas Pahune
import tkinter as tk
from random import randrange
import tkinter.font as font
from tkinter import messagebox
from tkinter import LabelFrame

window = tk.Tk()
window.title("Guessing Game")
window.config(bg="#41aea9")
myFont = font.Font(family='Comic Sans MS Bold')
window.iconbitmap(r"D:\software/python/endsem_1/favicon.ico")
# Constantia Bold
# Comic Sans MS Bold
lblInst_frame = LabelFrame(window, border=5, width=300, height=45, bg="teal")
lblInst_frame.place(x=268, y=26)
lblInst = tk.Label(window, text="Guess a number from 0 to 9",
                   bg="#41aea9", fg="#e8ffff", font=myFont)
lblLine0_frame = LabelFrame(window, border=5, width=240, height=45, bg="teal")
lblLine0_frame.place(x=130, y=155)
lblLine0 = tk.Label(window, text="---------------------------------------------------------------------",
                    bg="#41aea9", fg="#e8ffff", font=myFont)
lblNoGuess_frame = LabelFrame(
    window, border=5, width=152, height=45, bg="teal")
lblNoGuess_frame.place(x=591, y=155)
lblNoGuess = tk.Label(window, text="No of Guesses: 0",
                      bg="#41aea9", fg="#e8ffff", font=myFont)
lblMaxGuess = tk.Label(window, text="Max Guess: 3",
                       bg="#41aea9", fg="#e8ffff", font=myFont)
lblLine1 = tk.Label(window, text="---------------------------------------------------------------------",
                    bg="#41aea9", fg="#e8ffff", font=myFont)
lblLogs = tk.Label(window, text="Score Board",
                   bg="#41aea9", fg="#e8ffff", font=myFont)
lblLine2 = tk.Label(window, text="---------------------------------------------------------------------",
                    bg="#41aea9", fg="#e8ffff", font=myFont)

# create the buttons
buttons = []


for index in range(0, 10):
    button = tk.Button(window, text=index, command=lambda index=index: process(
        index), state=tk.DISABLED, bg="#41aea9", fg="#e8ffff", font=myFont, padx=15, pady=15)
    buttons.append(button)


btnStartGameList = []
for index in range(0, 1):
    btnStartGame = tk.Button(window, text="Start Game", command=lambda: startgame(
        index), bg="#41aea9", fg="#e8ffff", font=myFont)  # lambda functions are one liner functions
    btnStartGameList.append(btnStartGame)

# append elements to grid
lblInst.grid(row=0, column=0, columnspan=5, pady=30)
lblLine0.grid(row=1, column=0, columnspan=5, pady=10)
lblNoGuess.grid(row=2, column=0, columnspan=3, pady=10)
lblMaxGuess.grid(row=2, column=3, columnspan=2, pady=10)
lblLine1.grid(row=3, column=0, columnspan=5, pady=10)
# row 4 - 8 is reserved for showing logs
lblLogs.grid(row=4, column=0, columnspan=5, pady=10)

lblLine2.grid(row=9, column=0, columnspan=5, pady=10)


for row in range(0, 2):
    for col in range(0, 5):
        i = row * 5 + col  # convert 2d index to 1d. 5= total number of columns
        buttons[i].grid(row=row+10, column=col, pady=10)

btnStartGameList[0].grid(row=13, column=0, columnspan=5, pady=20)

# Main game logic

guess = 0
totalNumberOfGuesses = 0
secretNumber = randrange(10)
print(secretNumber)
lblLogs = []
guess_row = 4

# reset all variables


def init():
    global buttons, guess, totalNumberOfGuesses, secretNumber, lblNoGuess, lblLogs, guess_row
    guess = 0
    totalNumberOfGuesses = 0
    secretNumber = randrange(10)
    print(secretNumber)
    lblNoGuess["text"] = "Number of Guesses: 0"
    guess_row = 4

    # remove all score on init
    for lblLog in lblLogs:
        lblLog.grid_forget()
    lblLogs = []


def process(i):
    global totalNumberOfGuesses, buttons, guess_row
    guess = i

    totalNumberOfGuesses += 1
    lblNoGuess["text"] = ("Number of Guesses: " + str(totalNumberOfGuesses))

    # check if guess match secret number
    if guess == secretNumber:
        lbl = tk.Label(window, text="Your guess was right. You won! :) ",
                       fg="green", bg="#41aea9", pady=10, font=myFont)
        lbl.grid(row=guess_row, column=0, columnspan=5)
        msg = messagebox.showinfo(
            "Winning message", "Your guess was right. You won! :)")
        lblLogs.append(lbl)
        guess_row += 1

        for b in buttons:
            b["state"] = tk.DISABLED
    else:
        # give player some hints
        if guess > secretNumber:
            lbl = tk.Label(
                window, text="Secret number is less than your current guess :)", fg="red", bg="#41aea9", pady=10, font=myFont)
            lbl.grid(row=guess_row, column=0, columnspan=5)
            lblLogs.append(lbl)
            guess_row += 1
        else:
            lbl = tk.Label(
                window, text="Secret number is greater than your current guess :)", fg="red", bg="#41aea9", pady=10, font=myFont)
            lbl.grid(row=guess_row, column=0, columnspan=5)
            lblLogs.append(lbl)
            guess_row += 1

    # game is over when max no of guesses is reached
    if totalNumberOfGuesses == 3:
        if guess != secretNumber:
            lbl = tk.Label(
                window, text="Max guesses reached. You lost! :)", fg="red", bg="#41aea9", font=myFont)
            lbl.grid(row=guess_row, column=0, columnspan=5, pady=10)
            lblLogs.append(lbl)
            guess_row += 1

        for b in buttons:
            b["state"] = tk.DISABLED

    buttons[i]["state"] = tk.DISABLED


status = "none"


def startgame(i):
    global status
    for b in buttons:
        b["state"] = tk.NORMAL

    if status == "none":
        status = "started"
        btnStartGameList[i]["text"] = "Retart Game"
    else:
        status = "restarted"
        init()
    print("Game started")


window.mainloop()
