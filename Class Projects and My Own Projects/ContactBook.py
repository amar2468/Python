# **********************************Contact Book***************************************
# Author: Amar Plakalo
# Date: 11 Feb 2021
# This contact book allows user to add their contacts. They first have to create their account so that the contacts are private to them
# and so no one else can see. This will allow multiple users to create accounts on this app and they can save and update their contacts
# whenever they want
import random
import sqlite3


connection_with_contact_book = sqlite3.connect('Contact_Book.db')

cursorForContactBook = connection_with_contact_book.cursor()


connection_with_contact_book.commit()
# Create a registration,login,verification and log off systems

# 1. Registration
def registration_system(list1,dict1):
    user_name = input("Enter your name so that you can register to use the Contact Book app: ")
    if user_name in list1:
        print("Username already exists. Try another one: ")
        registration_system(list1,dict1)
    elif user_name not in list1:
        user_phone_number = input("Enter your phone number: ")
        user_password = input("Enter your password: ")
    returned_value = verification_process(user_password)

    if returned_value == 1:
        print("Thanks for registering " + user_name + ". Now, log on: ")
        list1.append(user_name)
        dict1[user_name] = user_password
        print(dict1) 
        print(list1)
        return user_name,user_phone_number,user_password
    elif returned_value == 0:
        print("Failed to register. Try again: ")
        registration_system(list1,dict1)


# 2. Log on system
def log_on_system(proof_of_log_on,user_name,user_password,list1):
    if proof_of_log_on == 0:
        print("Hello! Welcome back. Enter your username and password to log on: ")

        input_user_name = input("Enter username: ")
        input_passwd = input("Enter password: ")

        if user_name in list1:
            if dict1[input_user_name] == input_passwd:
                print("Welcome back to your account. Enjoy yourself!!!")
                proof_of_log_on = 1
                return proof_of_log_on
            else:
                print("Incorrectly entered username OR password OR both. Try again: ")
                proof_of_log_on = 0
                return proof_of_log_on
        else:
            print("The username you specified has not been created. Therefore, you cannot log on until you create an account: ")
            proof_of_log_on = 0
            return proof_of_log_on
    elif proof_of_log_on == 1:
        print("You are already logged in. You first have to log off in order to login. ")
        proof_of_log_on = 1
        return proof_of_log_on


# 3. Verify that this is you
def verification_process(passwd_user):
    code_received = random.randint(10000,99999) # random 5 digit number for the access code
    print("Your access code is " + str(code_received) + ".Enter this number and then enter your password to gain access: ")

    user_enter_code_received = input()

    if int(user_enter_code_received) == code_received:
        print("Well done. Correct code. Now enter your password: ")
        verify_pass = input()

        if verify_pass == passwd_user:
            print("You are logged in. Thanks for creating this account on our app!!")
            number_to_return = 1
            return number_to_return
        else:
            print("Incorrect password.")
            number_to_return = 0
            return number_to_return
    else:
        print("Incorrect code inputted. The code has now expired.")
        number_to_return = 0
        return number_to_return

# 4. Log off System
def log_off_system(check_log_on):
    if check_log_on == 1:
        user_log_off = input("Do you wish to log off? Y or N: ")
        if user_log_off.startswith("Y") or user_log_off.startswith("y"):
            print("See you next time!!!")
            check_log_on = 0
            return check_log_on   
        elif user_log_off.startswith("N") or user_log_off.startswith("n"):
            print("Ok. Carry on using the app with your account!!!")
            check_log_on = 1
            return check_log_on
    elif check_log_on == 0:
        print("You cannot log off because you have not logged on. First log on before you want to log off: ")
        check_log_on = 0
        return check_log_on
def add_contact(check_log_on):
    if check_log_on == 1:
        name_of_person = input("Enter the name of the person you wish to add to your contact book: ")
        address_of_person = input("Enter the address of the person you wish to add: ")
        phone_number_of_person = input("Enter the phone number of the person: ")
        email_of_person = input("Enter the email of the person: ")
        cursorForContactBook.execute("INSERT INTO contact_book_users VALUES (?,?,?,?)",(name_of_person,address_of_person,phone_number_of_person,email_of_person))
    elif check_log_on == 0:
        print("You first have to login in order to add a contact: ")
def remove_contact(check_log_on):
    if check_log_on == 1:
        user_id = input("Enter the id of the user you wish to delete: ")
        cursorForContactBook.execute("DELETE FROM contact_book_users WHERE rowid = (?)",user_id)
    elif check_log_on == 0:
        print("You are not logged on - so you cannot check remove the contact: ")
def view_contact(check_log_on):
    if check_log_on == 1:
        cursorForContactBook.execute("SELECT rowid,* FROM contact_book_users")
        print(cursorForContactBook.fetchall())
    elif check_log_on == 0:
        print("You cannot view the contacts because you are not logged on: ")


menu_choice = 0
check_log_on = 0
list1 = []
dict1 = {}
while menu_choice != 1 and menu_choice != 2 and menu_choice != 3 and menu_choice != 4 and menu_choice != 5 and menu_choice != 6:
    print("Welcome. Pick an option from the menu: ")
    print("1.Register an account: ")
    print("2.Log into your account: ")
    print("3.Add a contact: ")
    print("4.Remove a contact: ")
    print("5.View a contact: ")
    print("6.Log off: ")
    try:
        menu_choice = int(input("Enter your choice: "))
    except ValueError:
        print("You need to choose an option from 1-6: ")
    else:
        if menu_choice == 1:
            if check_log_on == 0:
                user_name,user_phone_number,user_password = registration_system(list1,dict1)
                menu_choice = 0 
            elif check_log_on == 1:
                print("You cannot create an account because you are already logged in. Log off and then you can create an account: ")
                menu_choice = 0
        elif menu_choice == 2:
            check_log_on = log_on_system(check_log_on,user_name,user_password,list1)
            menu_choice = 0
        elif menu_choice == 3:
            add_contact(check_log_on)
            menu_choice = 0
        elif menu_choice == 4:
            remove_contact(check_log_on)
            menu_choice = 0
        elif menu_choice == 5:
            view_contact(check_log_on)
            menu_choice = 0
        elif menu_choice == 6:
            check_log_on = log_off_system(check_log_on)
            menu_choice = 0
