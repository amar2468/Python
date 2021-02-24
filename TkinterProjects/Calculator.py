#-------------------------------------------Complex Calculator---------------------------------------------------
# Author: Amar Plakalo
# Date: 24 February 2021
# Used Visual Studio Code on Windows 10


import tkinter
from tkinter import Tk,Button,Entry
from tkinter.constants import END

root = Tk()
root.title("Complex Calculator")
root.geometry("327x420")

entry_box = Entry(root,font="30")
entry_box.grid(row = 0, column = 0,columnspan = 4,ipadx=50,ipady=10)

def click_modulus():
    entry_box.insert(0,"%")
def click_CE():
    entry_box.delete(0,END)
def click_C():
    entry_box.delete(0,END)
def click_del():
    entry_box.delete(0)
def click_opening_bracket():
    entry_box.insert(0,"(")
def click_closing_bracket():
    entry_box.insert(0,")")
def click_button_squared():
    entry_box.insert(0,"^")
def click_division():
    entry_box.insert(0,"/")
def click_button_multiply():
    entry_box.insert(0,"*")
def click_button_plus():
    entry_box.insert(0,"+")
def click_button_minus():
    entry_box.insert(0,"-")
def click_button_number(number_entered):
    save_number = entry_box.get()
    entry_box.delete(0,END)
    entry_box.insert(0,str(save_number) + str(number_entered))


button_modulus = Button(root,text="%",padx=30,pady=25,command=click_modulus)
button_CE = Button(root,text="CE",padx=29,pady=25,command=click_CE)
button_C = Button(root,text="C",padx=31,pady=25,command=click_C)
button_del = Button(root,text="del",padx=30,pady=25,command=click_del)

button_opening_bracket = Button(root,text="(",padx=33,pady=25,command=click_opening_bracket)
button_closing_bracket = Button(root,text=")",padx=34,pady=25,command=click_closing_bracket)
button_squared = Button(root,text="x^2",padx=26,pady=25,command=click_button_squared)
button_division = Button(root,text="/",padx=35,pady=25,command=click_division)


button_7 = Button(root,text="7",padx=33,pady=25,command=lambda:click_button_number(7))
button_8 = Button(root,text="8",padx=33,pady=25,command=lambda:click_button_number(8))
button_9 = Button(root,text="9",padx=32,pady=25,command=lambda:click_button_number(9))
button_multiply = Button(root,text="X",padx=34,pady=25,command=click_button_multiply)

button_4 = Button(root,text="4",padx=33,pady=25,command=lambda:click_button_number(4))
button_5 = Button(root,text="5",padx=33,pady=25,command=lambda:click_button_number(5))
button_6 = Button(root,text="6",padx=32,pady=25,command=lambda:click_button_number(6))
button_minus = Button(root,text="-",padx=35,pady=25,command=click_button_minus)

button_1 = Button(root,text="1",padx=33,pady=25,command=lambda:click_button_number(1))
button_2 = Button(root,text="2",padx=33,pady=25,command=lambda:click_button_number(2))
button_3 = Button(root,text="3",padx=32,pady=25,command=lambda:click_button_number(3))
button_plus = Button(root,text="+",padx=34,pady = 25,command=click_button_plus)


button_modulus.grid(row=1 ,column = 0)
button_CE.grid(row = 1, column = 1)
button_C.grid(row = 1,column = 2)
button_del.grid(row = 1, column = 3)

button_opening_bracket.grid(row=2,column = 0)
button_closing_bracket.grid(row=2,column=1)
button_squared.grid(row=2,column = 2)
button_division.grid(row=2,column = 3)

button_7.grid(row=3,column = 0)
button_8.grid(row=3,column = 1)
button_9.grid(row=3,column=2)
button_multiply.grid(row=3,column= 3)

button_4.grid(row=4,column = 0)
button_5.grid(row=4,column = 1)
button_6.grid(row=4,column = 2)
button_minus.grid(row=4,column =3)

button_1.grid(row=5,column=0)
button_2.grid(row=5,column=1)
button_3.grid(row=5,column=2)
button_plus.grid(row=5,column=3)

root.mainloop()
