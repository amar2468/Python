**************************************************Dice Simulation**************************************************

This file contains the documentation about the mini-project that I created in the Tkinter library in python called DiceSimulation.py

Firstly, some libraries are used so that this mini-project can work. Tkinter was imported because it is needed in this mini-project for the GUI aspect. From the tkinter library, a Tk, button and label were imported because a button is to throw the dice. The label is needed as a heading in the GUI. Finally, the Tk() opens the window. 

The root.iconbitmap sets the icon in the window as a picture of a small dice. This is a logo that is located at the top left part of the window.

The title basically is the heading given to the window that opens. Then, a label was created as I mentioned above that is the heading of the GUI program. 

In order to make the program throw the dice, six pictures of the dice are needed. ImageTk.photoimage() is a command that allows the picture to be seen in the GUI. All of these images are then put inside a list so that they can be accessed. 

The button was then created so that the user can roll the dice. Once they roll the dice, the random library is used and a function to take a random image from the list is used. Then, this image is presented to the screen so the user can see the dice number. 
