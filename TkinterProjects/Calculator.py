from tkinter import *

root = Tk() # this is used so that the window is displayed

root.title("My Calculator")

root.configure(bg='yellow')


my_entry = Entry(root,width = 30,font='12', borderwidth = 15)
my_entry.grid(row = 0, column = 0, columnspan = 4,padx=15,pady = 15)

def button_click(number):
    my_number = my_entry.get()
    my_entry.delete(0,END)
    my_entry.insert(0,str(my_number) + str(number))

def button_multiply():
    first_num = my_entry.get()
    global store_number
    global name_of_operation
    name_of_operation = "multiply"
    store_number = int(first_num)
    my_entry.delete(0,END)
def button_minus():
    first_num = my_entry.get()
    global store_number
    global name_of_operation
    name_of_operation = "minus"
    store_number = int(first_num)
    my_entry.delete(0,END)
def button_division():
    first_num = my_entry.get()
    global store_number
    global name_of_operation
    name_of_operation = "division"
    store_number = int(first_num)
    my_entry.delete(0,END)
def button_equal():
    second_num = my_entry.get()
    my_entry.delete(0,END)

    if name_of_operation == "plus":
        my_entry.insert(0,int(store_number) + int(second_num))
    elif name_of_operation == "multiply":
        my_entry.insert(0,int(store_number) * int(second_num))
    elif name_of_operation == "minus":
        my_entry.insert(0,int(store_number) - int(second_num))
    elif name_of_operation == "division":
        my_entry.insert(0,int(store_number) / int(second_num))
def button_plus():
    first_num = my_entry.get()
    global store_number
    global name_of_operation
    name_of_operation = "plus"
    store_number = int(first_num)
    my_entry.delete(0,END)
def button_clr():
    my_entry.delete(0,END)
def button_delete_last_number():
    my_entry.delete(0)

btn_7 = Button(root,text="7",font='12',padx=35,pady=25,bg='grey',command=lambda:button_click(7))
btn_8 = Button(root,text="8",font='12',padx=35,pady=25,bg='grey',command=lambda:button_click(8))
btn_9 = Button(root,text="9",font='12',padx=35,pady=25,bg='grey',command=lambda:button_click(9))

btn_4 = Button(root,text="4",font='12',padx=35,pady=25,bg= 'grey',command=lambda:button_click(4))
btn_5 = Button(root,text="5",font='12',padx=35,pady=25,bg= 'grey',command=lambda:button_click(5))
btn_6 = Button(root,text="6",font='12',padx=35,pady=25,bg='grey',command=lambda:button_click(6))

btn_1 = Button(root,text="1",font='12',padx=35,pady=25,bg='grey',command=lambda:button_click(1))
btn_2 = Button(root,text="2",font='12',padx=35,pady=25,bg='grey',command=lambda:button_click(2))
btn_3 = Button(root,text="3",font='12',padx=35,pady=25,bg='grey',command=lambda:button_click(3))
btn_0 = Button(root,text="0",font='12',padx=35,pady=25,bg='grey',command=lambda:button_click(0))

btn_multiply = Button(root,text="*",font='12',padx=35,pady=25,bg='white',command=button_multiply)
btn_minus = Button(root,text="-",font='12',padx=35,pady=25,bg='white',command=button_minus)
btn_plus = Button(root,text="+",font='12',padx=33,pady=25,bg='white',command=button_plus)
btn_equal = Button(root,text="=",font='12',padx=35,pady=25,bg='white',command=button_equal)
btn_division = Button(root,text="/",font='12',padx=35,pady=25,bg='white',command=button_division)

btn_clr = Button(root,text="clr",font='12',padx=31,pady=25,bg='orange',command=button_clr)
btn_delete_last_number = Button(root,text="del",font='12',padx=31,pady=25,bg='orange',command=button_delete_last_number)



btn_7.grid(row=1,column=0)
btn_8.grid(row=1,column = 1)
btn_9.grid(row=1,column=2)

btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column = 1)
btn_6.grid(row=2,column=2)

btn_1.grid(row=3,column=0)
btn_2.grid(row=3,column = 1)
btn_3.grid(row=3,column=2)
btn_0.grid(row=4,column=1)

btn_multiply.grid(row=1,column=3)
btn_minus.grid(row=2,column = 3)
btn_plus.grid(row=3,column=3)
btn_equal.grid(row=4,column=2)
btn_clr.grid(row=4,column = 0)
btn_division.grid(row=4,column=3)
btn_delete_last_number.grid(row=5,column=0)


root.mainloop()
