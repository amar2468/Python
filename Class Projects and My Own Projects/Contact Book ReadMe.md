This contains documentation about the project ContactBook.py. This is my own coding project that I worked on. It is a contact book that holds the list of contacts and you can add contacts, remove contacts or update them. Each user who wishes to use this contact book must register and then login. The information is kept in a separate that only the specific user has access to.

Information about imports in my program:

I imported five libraries in my program. The reason why is because each library contains a function that is useful for this project. The random library would be used to generate a number for the verification code. The sqlite3 library was used to create a database that would have a table. The json library was needed because I needed to put variables and data structures into the file. The OS library was needed so that I could calculate the size of the file. If the user has just registered and logged in and they never had a contacts lists, the program would know that and create a new file for the user. Finally, the RE library was used to validate the email address.

Registration System function:

The registration_system() function allows the user to register using their name, phone number and password.There is some error checking involved such as checking whether the user name or password already exists.Once the user enters correct information, they are sent to another function called verification_process() and they have to confirm some details in order to properly register. If verification was successful, the username and password are added into the text file and values are returned. Otherwise, the user is sent back to register again.

Log on System function

The log_on_system() function allow the user to login using their username and password. There are error checking mechanisms which verify whether the username and password is entered correctly. If the account does not exist and the user tries to login, the systems tell them that their account doesn't exist.

Verification process function:

The verification_process() function checks whether the user is really the owner of the phone number. If they correctly input the verification code, they register successfully. Otherwise, their registration process fails.

Add contacts function:

The add_contact() function adds the contact that the user wants. Error checking is included when the email of the person is entered The user connects with their own database and if their database is empty, a table is created and values that the user inputs are added to the contact list. If the database is not empty, the values are added i.e. the contact is added.

Remove contacts function:

This function removes a contact, if the user wishes to do so. The user enters the contact id and the entry is deleted.

Update contacts function

The update_contact() function allows the user to update the contact that they have already added to the list. The function first checks whether the user has logged in. If they have, it connects with the user's database. Then, the file size is measured. If the file is completely empty, then the user cannot update the contacts. Otherwise, they put the person id that they wish the change and then, they choose which information they want to change. After picking an option, the UPDATE sqlite3 command is executed and the information is changed. If the user did not log on, they will get an error message and they will be returned back to the main menu.

View contacts function

This function allows the user to view the contact list and to see the total amount of contacts they have. This is done by connecting to the user database, creating a cursor and using fetchall() and a for loop to see all the contact that the user has.

Log off function

This function checks whether the user has already logged on. If they have, they will the user whether they want to log off or not. If the user has not logged on, the program will not allow this function to run until someone logs on.

Menu

In the menu, the user can pick from 8 options. They must enter an integer in order for the menu choice to be valid. Nearly every menu choice calls a function that executes a particular task. If the user enters something invalid or they do something with is incorrect (i.e. they try to register while they are logged in), then the user will be presented with an error message that tells them this. 

User Manual - How to use this program?

First, ensure you have an IDE and compiler that can run python. Then, when you run the code, a menu will appear. Choose the option you want. Once you exit the program, if you havre registered before, the program will remember you the next time you come. In that case, you go to option 2 and log in. You cannot login if you have not registered an account. If you have already registered and logged in, then you can add a contact. You enter the details of the person and their contact will be added. If you want to remove a contact, you will be asked to enter the ID of the person you wish to delete. If you choose option 5, you can update an already inserted contact. For this, you must enter the ID of the person you are updating and what exact detail you want to change (i.e. address, phone number, etc...). If you choose option 6, the list of contacts will be presented to you and the number of contacts that you have will be at the top of the list. If you choose option 7, it will ask you whether you wish to log off. If you don't wish to log off, you can say 'n'. If yes, say 'y'. If you haven't logged in, you cannot log off. Finally, if you pick option 8, the program will exit completely. If you made changes to the database such as adding contacts, removing them or updating them, this will be saved and you can do it again the next time you log in.
