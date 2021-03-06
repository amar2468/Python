# Document Retrieval Assignment which will ask user to enter search words and it will present the user with the documents in which the words 
# appear in. The user can then see the document and read it if they want. Once they are done, they can repeat the process or they can end the 
# program using the quit button
# Author: Amar Plakalo
# Date: 05/05/2021 (Last Updated)
# Used Visual Studio Code on Windows 10
import string

import tkinter
from tkinter import Tk,Button,Entry,Label,messagebox,Text
from tkinter.constants import END



def divide_into_documents(my_file): # This function takes the file as the parameter and divides the documents in the file into the list

    current_document = '' # I started off with an empty string so that I can concatenate each line into it from the document until the token
    list1 = [] # empty list that will hold all the documents
    new_token = '<NEW DOCUMENT>' # string2 has been set to that value so that when I approach the token, I can skip to the next line

    for i in my_file: # iterates over the file using i
        if new_token not in i:  
            current_document = current_document + i 
            pass
        else: # if we encounter the token
            if current_document == '': # if the string is empty 
                pass 
            else: # in the case that there are elements in the string i.e. it is filled with elements
                for i in current_document: # for each element in the string
                    if i in string.punctuation and i != '.': # if that element is a member of string.punctuation
                        current_document = current_document.replace(i, '') # replace it with ''
                list1.append(current_document) # this adds the string to the list
                current_document = '' # once you add the string to the list, you empty the string so that you can continue on
            pass
    # This last for loop is there because after the last <NEW DOCUMENT>, there is no more <NEW DOCUMENT> and it is not added to the list
    # With this, I simply append the string to the list when the document is finished.

    for i in current_document: # this is similar to the one above in the else statement. The reason why we have one here is because the last document needs to be added to the list and we are already outside the loop because there is no more token
        if i in string.punctuation and i != '.': # if i is a member of string.punctuation
            current_document = current_document.replace(i, '') # replace it with ''
    list1.append(current_document) # append the string to the list

    return list1 # return the list

def add_to_dictionary(list1): # Function that passes the list and this function will add the elements from the list into the dictionary

    dictionary1 = {} # we start off with an empty dictionary

    j = 0   # value of j is set to 0

    counter = 0 # counter is set to 0

    i = 0 # i is set to 0
    splitted_into_words = list1[i].split() # i splitted the first document in the list so that i can add each word into the dictionary
    for splitted_into_words in list1: # iterates over the words in the list
        if i < len(list1): # will run until the end of the list
            splitted_into_words = list1[i].split() # splits the next element in the list
        else:
            pass
        while counter < len(splitted_into_words): # this will run until counter is not less than the length of the element
            if splitted_into_words[j] in dictionary1: # if the word is in the dictionary
                dictionary1[splitted_into_words[j].lower()] = dictionary1[splitted_into_words[j]] + [i + 1] # add the current document number to the the value of the key
                j += 1 
                counter += 1
            else:
                dictionary1[splitted_into_words[j].lower()] = [i + 1] # add the document number to the word that is the key
                j += 1
                counter += 1
        else: # when finished iterating over the element
            i += 1 # increase the element index by 1
            j = 0
            counter = 0
    return dictionary1 # return the dictionary

    
def find_word_in_document(dictionary1,wordsEntered): # function that passes three parameters which finds where the word is in the document
    
    if wordsEntered == "":
        messagebox.showerror("Error: Text Not Entered","You haven't entered words. You must enter at least one word. Try again!")
    else:
        newWindow = Tk()
        newWindow.title("Search Words")
        newWindow.geometry("500x513")
        newWindow.configure(bg="#ff8000")

        textBox = Text(newWindow, height = 80, width = 150)
        textBox.place(x=0,y=0)

        wordsEntered = wordsEntered.split()

        list_storing_sets = []

        inter_set = set() # this will hold the intersection of the two sets

        for i in range(0,len(wordsEntered)):
            for k in dictionary1.keys(): # iterates over each key in the dictionary
                if k == wordsEntered[i].lower(): # if the key in the dictionary is equal to the word entered by the user
                    list_storing_sets.insert(i,set(dictionary1[k]))
                    textBox.insert("0.0","\n" + k + " -> " + str(list_storing_sets[i]) + "\n")
                else:
                    continue
        if len(list_storing_sets) <= 1:
            if inter_set == set(): # if there is no intersection
                messagebox.showinfo("No intersection between words","There are no documents that are common between these words!")
            else: # otherwise
                textBox.insert(END,"\n" + "\nIntersection -> " + str(inter_set))
        else:
            inter_set = set.intersection(*list_storing_sets)

            if inter_set == set(): # if there is no intersection
                messagebox.showinfo("No intersection between words","There are no documents that are common between these words!")
            else: # otherwise
                textBox.insert(END,"\n" + "\nIntersection -> " + str(inter_set))
def print_document(listPassed,documentChosen):

    if documentChosen == "" or documentChosen >= 'a' and documentChosen <= 'z' or documentChosen >= 'A' and documentChosen <= 'Z':
        messagebox.showerror("Error: No Number Entered","You haven't selected a document number. Try again!")
    elif int(documentChosen) > len(listPassed):
        messagebox.showerror("Error: Document Number Does Not Exist","Document number entered does not exist. Try again!")
    else:
        windowTwo = Tk()
        windowTwo.title("Present Documents")
        windowTwo.geometry("560x545")
        windowTwo.configure(bg="#ff8000")

        printDocumentBox = Text(windowTwo, height = 80, width = 150)
        printDocumentBox.place(x=0,y=0)

        documentChosen = int(documentChosen)
        documentChosen = documentChosen - 1
        printDocumentBox.insert("0.0",str(listPassed[documentChosen]))


# Root window which display buttons, labels, etc.. This is the main GUI window

root = Tk()
root.title("Document Retrieval App")
root.geometry("500x513")
root.configure(bg="#42e3f5")

# open the file and put it inside the variable

my_file = open('ap_docs.txt','r')


# empty list declared

list1 = []


# call the function that divides the file into documents

list1 = divide_into_documents(my_file)

# Calls the function which adds the words to the dictionary from the list passed.

dictionary1 = add_to_dictionary(list1)


# Below is the GUI for this app. Labels, Entry boxes, Buttons and Frames were used in order to make this app functional

# The label shows the user the title of the app and it is inside the window.

label = Label(root,text="Welcome to the Document Retrieval App! Enjoy yourself!!!",font=('Comic Sans MS', 13,'bold'),bg="#42e3f5").place(x=10,y=10)
label_search_for_word = Label(root,text="Search For Words",font=('Comic Sans MS', 12,'bold'),bg="#42e3f5",fg="#006e24").place(x=100,y=70)
label_find_document = Label(root,text="Find Document",font=('Comic Sans MS', 12,'bold'),bg="#42e3f5",fg="#006e24").place(x=100,y=210)
# This is a textfield which allows the user to enter the words they wish to search for. The second command stores a placeholder
# which tells the user what they have to do, which in this case is to enter words to search for. The third command is a button
# that searches for the words entered.

TypeInWords = Entry(root,width = 23,font="Times")
TypeInWords.insert(0,"Type words you wish to find")
SearchButtonToFindDocs = Button(root,text = "Search",padx=20,pady=10,bg = "#A9A9A9",font=('Comic Sans MS', 12),command=lambda:find_word_in_document(dictionary1,TypeInWords.get()))


# Entry box which allows the user to input the document number they wish to preview. The second command is a placeholder that explains
# to the user what they must enter in the textfield
# When the button below is clicked, the document number entered will be passed to the print_document() function as well as the list of 
# documents. Then, the document number will be an index inside the list minus 1 because indexes start from 0 in python. So if the 
# user enters document number = 2, that will be index = 1. 

EnterDocumentNumber = Entry(root,width=20,font="Times")
EnterDocumentNumber.insert(0,"Enter document number")
ReadDocuments = Button(root,text = "Read Documents",padx=10,pady=10,bg = "#A9A9A9",font=('Comic Sans MS', 12),command=lambda:print_document(list1, EnterDocumentNumber.get()))


# Quit program button allows the user to exit the app. It immediately closes the root window.

QuitProgram = Button(root,text="Quit Program",padx=10,pady=10,bg = "#A9A9A9",font=('Comic Sans MS', 12),command= root.destroy)


# Using layout type "place" which allows me to place exactly where I want a widget to appear using x,y coordinates.
# The below is done for the search box to enter words to search and the button which searches for those words

TypeInWords.place(x=100,y=100)

SearchButtonToFindDocs.place(x=100,y=130)

# Using layout type "place" which allows me to place exactly where I want a widget to appear using x,y coordinates.
# The below is done for the document number search to enter the document number to search and the button which searches for the document
# number entered

EnterDocumentNumber.place(x=100,y=240)

ReadDocuments.place(x=100,y=270)

# Using layout type "place" which allows me to place exactly where I want a widget to appear using x,y coordinates.
# The below is done for the quit program button which, when clicked, exits the app

QuitProgram.place(x=369,y=455)

# Closes the file

my_file.close()

# Window appears and does not close until the user wants to exit.

root.mainloop()
