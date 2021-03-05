PROJECT NAME - DOCUMENT-RETRIEVAL

Author: Amar Plakalo

The document-retrieval.py file is a simple program that works similar to a web search engine. The only difference is that it is much more simpler than a web search engine.
ap_docs.txt file is filled with documents that are separated by a <NEW DOCUMENT> token
  
The aim of this program is for the user to enter two words and the program will look for where these words are located i.e. in which documents.
The program has three options: 
                                1. Search for Documents
                                2. Read Documents
                                3. Quit Program
                               
The first option asks the user to enter two words that they wish to look for. The program then identifies where these words are located i.e. which documents.
Sets are used for these two words and then an intersection set is used to find the common documents between the two words.
Option 2 asks the user which document they wish to see. The user enters the document and it is presented to the user to see.
Option 3 is if the user wishes to exit the program. A thank you message is printed and the program ends.
  

The project is details is as follows:

FUNCTION DIVIDE_INTO_DOCUMENTS

For my program, I first opened the file and made the mode “r” which means read. Then, I declared an empty list which would store the documents inside it. I then called the function and passed the file into it so that I can divide the file into documents. Inside the function, I created an empty string (current_document) and a string that contained the start of the token (new_token). I iterated over the file using i. I joined the string to the value in i using concatenation and I stripped the punctuation using "import string" and i used the string.punctuation function so that it does not contain weird characters. After this, I created an else that would execute the code if new_token symbol was in i. If the current_document was empty, it would just continue on and ignore it. Otherwise, the current_document would be appended to the list1.

FUNCTION ADD_TO_DICTIONARY

Then, I called the dictionary function which would add words to the dictionary and add document numbers relevant to the word. I started off with an empty dictionary. I then split the list at the start so that the first document in the list would be looked at word by word and added to the dictionary. Then, I iterated over the words in the document. There was an if statement that basically looks at whether the value of i is less than the length of the list1. If it is, it splits the next document in the list. At that stage, we move on to the while loop that iterates over the length of the document. If the word is already in the dictionary, I add the document number to the set of the document numbers. I increment some values. In the case that the word is not in the dictionary, I concatenated the document number to the set. Once the while loop completes, I increase i by 1 because I want to move on to the next document and I set j and counter to 0 because they are set back to what they were at the beginning. Finally, I return the dictionary.

FUNCTION FIND_WORD_IN_DOCUMENT

When I called the function that searches the words in the documents from menu option 1, I declared 2 empty sets and one intersection set that would hold the common documents between the words. I first iterated over all the keys in the dictionary. If the key was equal to the word, I put the document number in the set. Once that was complete, I looked for the intersection between the two sets. If there was no intersection, meaning that no documents were common between them, then a message was printed. Otherwise, a list of common documents was printed to screen.

THE MENU

Now, I moved on to the menu. Firstly, I set the value of user_input to 0 so that the menu option would be 0 at the start because the menu has not yet been used. I presented a menu to the user and they had three options. If they chose option 1, they would enter their 2 search words and the function would be called. I used try/except to error check for potential errors such as not entering two words. The try part tries to do what is inside it. The except part is executed if the error specified occurs. The else part runs if the try was successful. The 2nd menu option looks for the document number and user types it in and the program gives them the document to read. I also included many error checks such as printing an error if the user wrote in words instead of using integers. When the 3rd menu option was executed, it thanked the user for using the program and ends. Then, I closed my file.
