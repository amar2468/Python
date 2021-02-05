# Program that simulates a dice when rolled. 
# Author - Amar Plakalo
# Date - 05/02/2021
import tkinter
from tkinter import Entry, Tk, Button, Label
from tkinter.constants import END
from PIL import Image,ImageTk

import random

root = Tk()
root.title("My Dice Rolling Program")

heading_in_the_game = tkinter.Label(root,text=" Welcome to this game. Have fun!!",bg="orange",font=15)
heading_in_the_game.grid(row=0,column=0,columnspan = 5)


my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/amar-/Desktop/Dice1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("C:/Users/amar-/Desktop/Dice2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/amar-/Desktop/Dice3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("C:/Users/amar-/Desktop/Dice4.png"))
my_img5 = ImageTk.PhotoImage(Image.open("C:/Users/amar-/Desktop/Dice5.png"))
my_img6 = ImageTk.PhotoImage(Image.open("C:/Users/amar-/Desktop/Dice6.png"))
image_list = [my_img1,my_img2,my_img3,my_img4,my_img5,my_img6]


def button_clicked():
    my_label = Label(image=random.choice(image_list))

    my_label.grid(row = 1, column = 1, columnspan = 3)

my_label = Label(image=my_img1)

my_label.grid(row = 1, column = 1, columnspan = 3)

click_button = Button(root, text="Roll the dice", command=button_clicked)

click_button.grid(row = 2, column = 2)

root.mainloop()
