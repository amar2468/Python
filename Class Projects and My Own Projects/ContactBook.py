# **********************************Contact Book***************************************
# Author: Amar Plakalo
# Date: 27 Feb 2021 Updated 21/03/2021
# This contact book allows user to add their contacts. They first have to create their account so that the contacts are private to them
# and so no one else can see. This will allow multiple users to create accounts on this app and they can add and remove contacts as they
# wish. They can also view their contacts and have access to information they need such as the phone number of the person. 

import random # this import will allow me to access functions from the library called random. I need a verification code which is a
              # random 5 digit number from 10000,99999
import sqlite3 # this import is needed so that I can add entries to the user database so that contacts can be retrieved.
import json # this is used so that variables and data structures can be put inside a file if needed
import os # this import is used when I need to calculate the size of the file
import re # this is used when i need to validate the email the user entered when they wish to add a contact

# Create a registration,login,verification and log off systems

# 1. Registration
def registration_system(dict1):
    """
    The registration_system() function allows the user to register using their name, phone number and password.
    There is some error checking involved such as checking whether the user name or password already exists.
    Once the user enters correct information, they are sent to another function called verification_process()
    and they have to confirm some details in order to properly register. If verification was successful, the
    username and password are added into the text file and values are returned. Otherwise, the user is sent 
    back to register again.
    """
    returned_value = 0 # allows verification to take place

    user_name = input("Enter your name so that you can register to use the Contact Book app: ") # enter the username
    user_phone_number = input("Enter your phone number: ") # enter the phone number
    user_password = input("Enter your password: ") # enter the password
    save_users_data = open("contactbookdetails.txt","r") # opens a text file with the "r" mode which means read
        
    for i in save_users_data: # iterate over the file
        password_and_username = json.loads(i) # store the value of i into password_and_username

        if user_name in password_and_username.keys(): # if the username is in the file i.e. account registered before
            if user_password in password_and_username.values(): # if the password is also in it i.e. same username and pass
                print("Username and password already exist: ") # error message
                returned_value = 0 # doesn't allow verification to take place
                return user_name,user_phone_number,user_password # return values
            else: # if only the username is the same
                print("Username already exists") # error message
                returned_value = 0 # stopping verification
                return user_name,user_phone_number,user_password # return the values
            
    else: # if everything went well
        returned_value = verification_process(user_password) # call the verification process
        
    
    if returned_value == 1: # if the value returned is 1
        print("Thanks for registering " + user_name + ". Now, log on: ") # thank you message
        dict1.clear() # clear the dictionary so that a new element can be inserted
        dict1[user_name] = user_password # insert new element

        save_users_data = open("contactbookdetails.txt","a") # append mode used for the existing file
        json.dump(dict1,save_users_data) # put the dictionary contents into the file
        save_users_data.write("\n") # tells the file to skip to the next line
        save_users_data.close() # closes file


        return user_name,user_phone_number,user_password # return values

    elif returned_value == 0: # if verification failed
        print("Failed to register. Try again: ") # error message
        registration_system(dict1) # call registration again


# 2. Log on system
def log_on_system(check_log_on):
    """
    The log_on_system() function allow the user to login using their username and password.
    There are error checking mechanisms which verify whether the username and password is entered correctly.
    If the account does not exist and the user tries to login, the systems tell them that their account doesn't exist
    """

    if check_log_on == 0: # if the user has not logged in yet
        print("Hello! Welcome back. Enter your username and password to log on: ")

        input_user_name = input("Enter username: ") # user enters their username
        input_passwd = input("Enter password: ") # user enters their password
        save_users_data = open("contactbookdetails.txt","r") # file is opened in read mode
        for i in save_users_data: # for each element in the file
            password_and_username = json.loads(i) # i is saved in password_and_username

            if input_user_name in password_and_username.keys(): # if the username already exists
                if password_and_username[input_user_name] == input_passwd: # if the password is correct
                    print("Welcome back to your account. Enjoy yourself!!!") # User has logged in
                    user_name = input_user_name # sets the value of the username entered as the username so that it can be referenced
                                                # in the program i.e. so the program knows who is logged on currently
                    check_log_on = 1 # sets the value to 1 meaning that the user has logged on
                    return check_log_on,user_name # return values
                else: # otherwise
                    print("Incorrectly entered username OR password OR both. Try again: ") # error message
                    check_log_on = 0 # user login set at 0 i.e. not logged in 
                    user_name = ""
                    return check_log_on,user_name # return the value
        else:
            print("User account that you entered does not exist on our system. Try again: ") # error message
            check_log_on = 0 # user not logged in
            user_name = ""
            return check_log_on,user_name # return value
                
    elif check_log_on == 1: # if user already logged in
        print("You already logged in: ") # error message
        proof_of_log_on = 1 # set value of login to 1
        user_name = ""
        return proof_of_log_on,user_name # return that value

# 3. Verify that this is you (Part of the registration process - in order to create your account to use the contact book)
def verification_process(passwd_user):
    """
    The verification_process() function checks whether the user is really the owner of the phone number.
    If they correctly input the verification code, they register successfully.
    Otherwise, their registration process fails.
    """
    code_received = random.randint(10000,99999) # random 5 digit number for the access code
    print("Your access code is " + str(code_received) + ".Enter this number and then enter your password to gain access: ")

    user_enter_code_received = input() # User enters code they received
    
    
    if int(user_enter_code_received) == code_received: # if the code that the user enters is equal to the code sent
        print("Well done. Correct code. Now enter your password: ") # code correct, now enter password
        verify_pass = input() # enters password

        if verify_pass == passwd_user: # if password is correct
            print("You have successfully verified your account. Thanks for creating this account on our app!!") # success
            number_to_return = 1 # return a 1 meaning that the verification process was a success
            return number_to_return # return the value
        else: # if password entered was incorrect
            print("Incorrect password.") # error message
            number_to_return = 0 # verification unsuccessful so value = 0
            return number_to_return # return that value
    else: # if the code is not equal to the original one
        print("Incorrect code inputted. The code has now expired.") # error message
        number_to_return = 0 # verification unsuccessful
        return number_to_return # return the value of 0

def add_contact(check_log_on,user_name):
    """
    The add_contact() function adds the contact that the user wants. Error checking is included when the email of the person is entered
    The user connects with their own database and if their database is empty, a table is created and values that the user inputs are
    added to the contact list. If the database is not empty, the values are added i.e. the contact is added.
    """
    if check_log_on == 1: # if the user is logged on
        name_of_person = input("Enter the name of the person you wish to add to your contact book: ")
        address_of_person = input("Enter the address of the person you wish to add: ")
        phone_number_of_person = input("Enter the phone number of the person: ")
        email_of_person = input("Enter the email of the person: ")
        regex = '^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$' # format of how the email should look like
        if (re.search(regex,email_of_person)): # using import re, the search function is used so that the program can verify whether the
                                               # email used is valid
            
            connection_with_user_database = sqlite3.connect('%s.db'% user_name) # connects with user's database
            cursorForUserBook = connection_with_user_database.cursor() # creates a cursor which is used to input details in the table
            filesize = os.path.getsize("%s.db"% user_name) # measures the size of the file
            str(phone_number_of_person)
            if filesize == 0: # if file is empty, create a table with the following:
                cursorForUserBook.execute("""CREATE TABLE contact_book_users(
                                        Name TEXT,
                                        Address TEXT,
                                        Phone TEXT,
                                        Email TEXT
                )""")

                cursorForUserBook.execute("INSERT INTO contact_book_users VALUES (?,?,?,?)"
                                        ,(name_of_person,address_of_person,phone_number_of_person,email_of_person)) # put the contact
                                                                                                            # into the file
                connection_with_user_database.commit() # saves changes
                connection_with_user_database.close() # close the database
            else:
                cursorForUserBook.execute("INSERT INTO contact_book_users VALUES (?,?,?,?)"
                                        ,(name_of_person,address_of_person,phone_number_of_person,email_of_person)) # put contact in the
                                                                                                                    # file
                connection_with_user_database.commit() # commit changes
                connection_with_user_database.close() # close the database
        else: # if incorrect email format was entered
            print("Invalid email entered: ") # error message
    elif check_log_on == 0: #if the user has not logged on yet
        print("You first have to login in order to add a contact: ") # Error message
def remove_contact(check_log_on):
    """
    This function removes a contact, if the user wishes to do so. The user enters the contact id and the entry is deleted
    """
    try: # attempt to connect with database of user
        connection_with_user_database = sqlite3.connect('%s.db'% user_name) 
    except NameError: # expect a name error which means that the username has not been created or the user didn't login
        print("The username does not exist or you have not logged in: ") # error message
    else: # if the connection to the database of the user was successful
        cursorForUserBook = connection_with_user_database.cursor() # create a cursor so that you can delete the entry
        if check_log_on == 1: # if the user is logged in
            user_id = input("Enter the id of the user you wish to delete: ") # ask which id they want to delete
            cursorForUserBook.execute("DELETE FROM contact_book_users WHERE rowid = (?)",(user_id,)) # deletes the id from the database
            connection_with_user_database.commit() # save the changes
            connection_with_user_database.close() # close the database
        elif check_log_on == 0: # if not logged in
            print("You are not logged on - so you cannot check remove the contact: ") # error message
def update_contact(check_log_on):
    """
    The update_contact() function allows the user to update the contact that they have already added to the list. The function first
    checks whether the user has logged in. If they have, it connects with the user's database. Then, the file size is measured.
    If the file is completely empty, then the user cannot update the contacts. Otherwise, they put the person id that they wish the change
    and then, they choose which information they want to change. After picking an option, the UPDATE sqlite3 command is executed and the
    information is changed. If the user did not log on, they will get an error message and they will be returned back to the main menu
    """
    if check_log_on == 1:
        connection_with_user_database = sqlite3.connect('%s.db'% user_name)
        filesize = os.path.getsize("%s.db"% user_name) # measures the size of the file
        if filesize == 0:
            print("You cannot update the contacts - you have not added any previously. You must do that first: ")
        else:
            cursorForUserBook = connection_with_user_database.cursor()
            person_id = input("Which contact ID do you wish to update?")
            update_choice = input("If you want to change the name, choose n or N. If you want to change the address, choose"
                                "a or A. If you wish to change the phone, choose p or P. If email, choose e or E: ")
            if update_choice.startswith("n") or update_choice.startswith("N"):
                new_name = input("Enter the new name: ")
                cursorForUserBook.execute("Update contact_book_users SET Name = (?) WHERE rowid = (?)",(new_name,person_id))
                connection_with_user_database.commit()
                connection_with_user_database.close()
            elif update_choice.startswith("a") or update_choice.startswith("A"):
                new_address = input("Enter the new address: ")
                cursorForUserBook.execute("Update contact_book_users SET Address = (?) WHERE rowid = (?)",(new_address,person_id))
                connection_with_user_database.commit()
                connection_with_user_database.close()
            elif update_choice.startswith("p") or update_choice.startswith("P"):
                new_phone_number = input("Enter the new phone number: ")
                cursorForUserBook.execute("Update contact_book_users SET Phone Number = (?) WHERE rowid = (?)",(new_phone_number,person_id))
                connection_with_user_database.commit()
                connection_with_user_database.close()
            elif update_choice.startswith("e") or update_choice.startswith("E"):
                new_email = input("Enter the new email: ")
                cursorForUserBook.execute("Update contact_book_users SET Email = (?) WHERE rowid = (?)",(new_email,person_id))
                connection_with_user_database.commit()
                connection_with_user_database.close()
    elif check_log_on == 0:
        print("You have to login in order to update the contacts. Please do so! ")
def view_contact(check_log_on):
    """
    This function allows the user to view the contact list and to see the total amount of contacts they have.
    This is done by connecting to the user database, creating a cursor and using fetchall() and a for loop to 
    see all the contact that the user has. 
    """
    try: # try to connect with the database
        connection_with_user_database = sqlite3.connect('%s.db'% user_name)
    except NameError: # expect a name error meaning that the user has not logged in or their account does not exist
        print("You haven't logged on or the account doesn't exist: ")
    else: # if the connection was successful
        cursorForUserBook = connection_with_user_database.cursor() # create a cursor so that you can use this when viewing contacts
        if check_log_on == 1: # if user has logged in
            filesize = os.path.getsize("%s.db"% user_name) # measure file size
            if filesize == 0: # if the file is empty
                print("You cannot view the contacts because your database of information has not been created"
                      "\nPlease add contacts in order for the account to function: ") # error message
            else: # if file not empty i.e. it is already created
                cursorForUserBook.execute("SELECT rowid,* FROM contact_book_users") # add a row id to each of the users
                contacts_saved_by_user = cursorForUserBook.fetchall() # fetchall() shows all the entries in a database
                number_of_contacts = 0 # set at 0 so that the program can see how many contacts there are
                while number_of_contacts < len(contacts_saved_by_user): # while the number of contacts (0) is less than the amount
                                                                        # of contacts in the actual database
                    number_of_contacts += 1 # increment it by 1
                print(number_of_contacts, "Contacts") # shows the total amount of contacts

                for each_contact in contacts_saved_by_user: # iterate over each contact
                    print(each_contact) # print it to screen

        elif check_log_on == 0: # if the user has not logged on
            print("You cannot view the contacts because you are not logged on: ") # error message
def log_off_system(check_log_on):
    """
    This function checks whether the user has already logged on. If they have, they will the user whether they want to log off
    or not. If the user has not logged on, the program will not allow this function to run until someone logs on
    """
    if check_log_on == 1: # if the user is already logged on
        user_log_off = input("Do you wish to log off? Y or N: ") # ask user do they want to log off
        if user_log_off.startswith("Y") or user_log_off.startswith("y"): # if yes
            print("See you next time!!!") # thank you message
            check_log_on = 0 # set the value to 0 meaning that the user has logged off
            return check_log_on # return this value
        elif user_log_off.startswith("N") or user_log_off.startswith("n"): # if the user says no
            print("Ok. Carry on using the app with your account!!!") # let them continue using the app
            check_log_on = 1 # set the value as 1 meaning they are logged in
            return check_log_on # return this value
    elif check_log_on == 0: # if user is not logged on
        print("You cannot log off because you have not logged on. First log on before you want to log off: ") # error message
        check_log_on = 0 # set the value to 0 meaning not logged on
        return check_log_on # return this value


menu_choice = 0 # the menu choice the user chooses
check_log_on = 0 # whether the user has logged on (1) or logged off (0)
number_of_contacts = 0 # counts the number of contacts the user has
dict1 = {} # stores the username and password
while menu_choice != 1 and menu_choice != 2 and menu_choice != 3 and menu_choice != 4 and menu_choice != 5 and menu_choice != 6 and menu_choice != 7 and menu_choice !=8:
    print("-----------------------------------")
    print("Welcome. Pick an option from the menu: ")
    print("1.Register an account: ")
    print("2.Log into your account: ")
    print("3.Add a contact: ")
    print("4.Remove a contact: ")
    print("5.Update a contact: ")
    print("6.View a contact: ")
    print("7.Log off: ")
    print("8.Exit the program: ")
    print("-----------------------------------")
    try: # allow user to enter a menu choice
        menu_choice = int(input("Enter your choice: "))
    except ValueError: # expect an error (user does not enter number from 1-8)
        print("You need to choose an option from 1-8: ")
    else: # otherwise
        if menu_choice == 1: # if the menu choice is 1
            if check_log_on == 0: # if the user is not logged on
                user_name,user_phone_number,user_password = registration_system(dict1) # call this function and it will return 
                                                                                       # all elements left of the equal sign
                menu_choice = 0 # go back to the main menu
            elif check_log_on == 1: # if the user is already logged on
                print("You cannot create an account because you are already logged in. Log off and then you can create an account: ")
                menu_choice = 0 # return back to main menu
        elif menu_choice == 2: # if user chooses option 2
            check_log_on,user_name = log_on_system(check_log_on) # call function and return variables on the left of the equal sign
            menu_choice = 0 # back to menu
        elif menu_choice == 3: # if the menu choice is 3
            try: # attempt to call the function to add a contact
                add_contact(check_log_on,user_name)
            except NameError: # expect that the user may not have logged in or an account may not be registered
                print("You haven't logged or your account has not been created: ")
                menu_choice = 0 # back to menu
            else: # otherwise if the user is already logged in
                menu_choice = 0 # return back to menu after adding the contact
        elif menu_choice == 4: # if user chose option 4
            remove_contact(check_log_on) # call the function to remove the contact
            menu_choice = 0 # back to menu
        elif menu_choice == 5: # if user wants to update contacts
            update_contact(check_log_on) # calls the function to update the contact
            menu_choice = 0 # back to the main menu
        elif menu_choice == 6: # if user chose option 6
            view_contact(check_log_on) # call the function that allows user to view the contact
            menu_choice = 0 # back to menu
        elif menu_choice == 7: # if the user chose option 7
            check_log_on = log_off_system(check_log_on) # call the log off function which will return the variable on the left of the
                                                        # equals sign
            menu_choice = 0 # back to menu
        elif menu_choice == 8: # option to exit out of the program
            print("Thanks for using the app! Bye: ") # thank you message printed to screen
