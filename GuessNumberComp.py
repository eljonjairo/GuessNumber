#!/usr/bin/env python3

# Guess the number (Computer) using an tkinter GUI
# Based on FreeCodeCamp.org
# John Diaz january 2023
#TO DO List:
#

import random
from tkinter import *

root = Tk()
g = Entry(root, width=80, borderwidth=7, bg="white", fg="black")
g.pack()


# Initialize the guess number
limit = random.randint(1,100)
number = random.randint(1,limit)

root.title(f" Enter a number between 0 and {limit}")

def btnF():
       # get the number in the box and substract with the actual number   
        x = int(g.get()) - number
        if x == 0:
             btnLabel = Label(root, text=g.get() + " is the right number!!!")             
        elif x > 0:
             btnLabel = Label(root, text=g.get() + " is too high...")             
        elif x < 0:
             btnLabel = Label(root, text=g.get() + " is too low...")             
        btnLabel.pack()        

btn = Button(root, text=" Check you guess !!!", command=btnF)
btn.pack()




root.mainloop()
