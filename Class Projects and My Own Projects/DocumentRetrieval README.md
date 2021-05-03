PROJECT NAME - DOCUMENT-RETRIEVAL

Author: Amar Plakalo

The document-retrieval.py file is a simple program that works similar to a web search engine. The only difference is that it is much more simpler than a web search engine.
ap_docs.txt file is filled with documents that are separated by a <NEW DOCUMENT> token
  
The aim of this program is for the user to enter two words and the program will look for where these words are located i.e. in which documents.
The program uses a GUI window to allow the user to either:
1. Search for the words
2. Read a document using the document number
3. Quit the program
                               
The first option asks the user to enter two words that they wish to look for. The program then identifies where these words are located i.e. which documents.
Sets are used for these two words and then an intersection set is used to find the common documents between the two words.
Option 2 asks the user which document they wish to see. The user enters the document and it is presented to the user to see.
Option 3 is if the user wishes to exit the program.

Note: If you wish to run this program, you must have a python IDE and compiler. Also, there is a file in this directory called ap_docs.txt. This is needed in this program because the program reads this file. When you want to run this program, ensure that the file is put inside the directory of where the python projects are.
  

The project is details is as follows:

FUNCTION DIVIDE_INTO_DOCUMENTS

For my program, I first opened the file and made the mode “r” which means read. Then, I declared an empty list which would store the documents inside it. I then called the function and passed the file into it so that I can divide the file into documents. Inside the function, I created an empty string (current_document) and a string that contained the start of the token (new_token). I iterated over the file using i. I joined the string to the value in i using concatenation and I stripped the punctuation using "import string" and i used the string.punctuation function so that it does not contain weird characters. After this, I created an else that would execute the code if new_token symbol was in i. If the current_document was empty, it would just continue on and ignore it. Otherwise, the current_document would be appended to the list1.

FUNCTION ADD_TO_DICTIONARY

Then, I called the dictionary function which would add words to the dictionary and add document numbers relevant to the word. I started off with an empty dictionary. I then split the list at the start so that the first document in the list would be looked at word by word and added to the dictionary. Then, I iterated over the words in the document. There was an if statement that basically looks at whether the value of i is less than the length of the list1. If it is, it splits the next document in the list. At that stage, we move on to the while loop that iterates over the length of the document. If the word is already in the dictionary, I add the document number to the set of the document numbers. I increment some values. In the case that the word is not in the dictionary, I concatenated the document number to the set. Once the while loop completes, I increase i by 1 because I want to move on to the next document and I set j and counter to 0 because they are set back to what they were at the beginning. Finally, I return the dictionary.

FUNCTION FIND_WORD_IN_DOCUMENT

The function takes in two parameters - dictionary of words and words that the user entered. The first thing that happens is that there is an error checking piece of code. If the user did not enter any text, the program tells the user that they didn't enter text. Otherwise, the new window is displayed and the text box widget is created. This will store the words that were searched for and what documents contain these words. I declared 2 empty sets and one intersection set that would hold the common documents between the words. I first iterated over all the keys in the dictionary. If the key was equal to the word, I put the document number in the set. Once that was complete, I looked for the intersection between the two sets. If there was no intersection, meaning that no documents were common between them, a message box was displayed to tell the user that there was no intersection. Otherwise, the intersection was shown.

FUNCTION PRINT_DOCUMENT

This function takes in 2 parameters - the list of documents and the document number entered by the user. There is an if...elif...else block that error checks. In the first if statement, the program checks whether there was nothing entered OR whether a letter was entered (instead of a number). If so, an error box pops up. Otherwise, if the document number entered is an integer but the document number does not exist, then the error message is displayed again. Otherwise, a new window is created which stores the Text box that will hold the contents of the document that the user chose. 

GUI

Firstly, a main GUI window is created with a certain size and a title and background colour. Then, the file is opened so that it can be read. A label is made which will be the title inside the GUI window so that the user knows what app this is. Then, there is an entry box that allows the user to enter words they wish to search for and a button that searches for these words. 

Then, there is an entry box which allows the user to enter the document number and a button that searches for this document number inside the list that contains the documents. An important thing to note is that the document number entered by the user will be subtracted by 1 because indexes start from 0 in python.

The last button is the quit button one which exits from the app when clicked.

Then, the layout style I chose was place(). This allows me to place a widget using x,y coordinates. I had to use place() for all the widgets that I chose to use. 
