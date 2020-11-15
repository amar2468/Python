# Document Retrieval Assignment which will ask user to enter search words and it will present the user with the documents in which the words 
# appear in. The user can then see the document and read it if they want. Once they are done, they can repeat the process or they can end the 
# program using menu opion 3
# Author: Amar Plakalo
# Date: 08/11/2020 (Last Updated)
# Used Visual Studio Code on Windows 10
import string

def divide_into_documents(my_file): # This function takes the file as the parameter and divides the documents in the file into the list

    string1 = '' # I started off with an empty string so that I can concatenate each line into it from the document until the token
    list1 = [] # empty list that will hold all the documents
    string2 = '<N' # string2 has been set to that value so that when I approach the token, I can skip to the next line

    for i in my_file: # iterates over the file using i
        if string2 not in i: # if i is inside the document 
            i = i.lower() # set i to lowercase
            string1 = string1 + ''.join(i.rstrip("\n")) + ' ' # concatenate the string and join the value i into the string. Also, I got rid of the \n using rstrip
            continue

        else: # if we encounter the token
            if string1 == '': # if the string is empty 
                continue 
            else: # in the case that there are elements in the string i.e. it is filled with elements
                for i in string1: # for each element in the string
                    if i in string.punctuation: # if that element is a member of string.punctuation
                        string1 = string1.replace(i, '') # replace it with ''
                list1.append(string1) # this adds the string to the list
                string1 = '' # once you add the string to the list, you empty the string so that you can continue on
            continue
    for i in string1: # this is similar to the one above in the else statement. The reason why we have one here is because the last document needs to be added to the list and we are already outside the loop because there is no more token
        if i in string.punctuation: # if i is a member of string.punctuation
            string1 = string1.replace(i, '') # replace it with ''
    list1.append(string1) # append the string to the list

    return list1 # return the list

def add_to_dictionary(list1): # Function that passes the list and this function will add the elements from the list into the dictionary

    dictionary1 = {} # we start off with an empty dictionary

    j = 0   # value of j is set to 0

    counter = 0 # counter is set to 0

    i = 0 # i is set to 0
    word = list1[i].split() # i splitted the first document in the list so that i can add each word into the dictionary
    for word in list1: # iterates over the words in the list
        if i < len(list1): # will run until the end of the list
            word = list1[i].split() # splits the next element in the list
        else:
            StopIteration
        while counter < len(word): # this will run until counter is not less than the length of the element
            if word[j] in dictionary1: # if the word is in the dictionary
                dictionary1[word[j]] = dictionary1[word[j]] + [i + 1] # add the current document number to the the value of the key
                j += 1 
                counter += 1
            else:
                dictionary1[word[j]] = [i + 1] # add the document number to the word that is the key
                j += 1
                counter += 1
        else: # when finished iterating over the element
            i += 1 # increase the element index by 1
            j = 0
            counter = 0
    return dictionary1 # return the dictionary

    

my_file = open('ap_docs.txt','r') # open the file and put it inside the variable

list1 = [] # empty list declared

list1 = divide_into_documents(my_file) # call the function that divides the file into documents


dictionary1 = add_to_dictionary(list1) # call the dictionary that adds elements to it

user_input = 0 # this is needed in the menu
def find_word_in_document(dictionary1,one_search_word,second_search_word): # function that passes three parameters which finds where the word is in the document
    a_set = set() # declare one empty set
    b_set = set() # declare another empty set
    inter_set = set() # this will hold the intersection of the two sets

    for k in dictionary1.keys(): # iterates over each key in the dictionary
        if k.lower() == one_search_word.lower(): # if the key in the dictionary is equal to the word entered by the user
            a_set = set(dictionary1[k.lower()]) # put the document number in the set
            print(k,'->',a_set) # print it to screen
        
        elif k.lower() == second_search_word.lower(): # if the key in the dictionary is equal to the second word entered by the user
            b_set = set(dictionary1[k.lower()]) # put document number in the set
            print(k,'->',b_set) # print to screen
        else:
            continue
    inter_set = a_set & b_set # find intersection between the documents i.e. the common documents

    if inter_set == set(): # if there is no intersection
        print("There are no documents found\n") # print message to screen
    else: # otherwise
        print(inter_set) # print the common documents

while user_input != 1 and user_input != 2 and user_input != 3: # while the user input is not 1 and 2 and 3
    print("\nWhat would you like to do? \n")
    print("1.Search for Documents: ")
    print("2.Read Documents: ")
    print("3.Quit Program: ")

    try: # try to enter the user_input which is the menu option
        user_input = int(input()) # force user to enter integer
    except ValueError:
        print("The value you entered is NOT an integer. Enter again please\n") # tell them to enter integer
        continue # loop back
    else:
        if user_input == 1: # menu option 1 is chosen
            try:
                one_search_word,second_search_word = input("Enter a word you wish to search for: ").split() # splits the words into two
            except ValueError:
                print("\nYou need to enter two words in. Please do so:\n")
                user_input = 0
            else:
                find_word_in_document(dictionary1,one_search_word,second_search_word) # calls function that takes three parameters
                user_input = 0 # set the user_input to 0 so that we return back to main menu
        
        elif user_input == 2: # if menu option 2 is selected
            try: # try to get user to enter document number which is an integer
                document_number = int(input("Enter document number: "))
            except IndexError: # expect an indexerror which means that the index written down does not exist
                print("There is no document with that number: ") # print error message
                user_input = 2 # return back to option 2
            except ValueError: # if the valueerror occurs
                print("The document number is not an integer\n") # print message that says that document number is not an integer
                user_input = 0 # return back to main menu
            else: # if the try succeeds
                print(list1[document_number - 1]) # print the list index that the user told them
                user_input = 0 # return to main menu
    
        elif user_input == 3: # if the menu option was 3
            print("Thanks for using document retrieval: ") # thank the user and end the program

my_file.close() # close the file

