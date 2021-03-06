This readme file shows all the relevant information about the project called FunGames.py

This project is made up of two games: Guessing number game and Rock paper scissors. The user can choose which game they wish to play. If they get enough wins in a certain amount of rounds, they win a prize. They can also try again if they are not happy. 

Firstly, the random library was imported. The reason why is because it is needed in the rock paper scissors game and in the number guessing game. For the rock paper scissors, it is needed so that the computer can play either of the three options while in the guessing game, it is needed in order to generate a random number within a range. 

GAME CLASS

The parent class called Games is created. This class will be inherited by other classes. The reason why is because number guessing game is a game and rock paper scissors is also a game. There is a direct connection between these. Let's step through each method:

In the __init__ method, a number of variables are initialised so that they can be used in the class. 

In the create_account() method, the user enters their name, their email and their password. Then, they are asked to input the email again to see whether the email they now entered matches the email that was accepted first. If yes, they are asked for a password. if they get it right, a thank you message is printed out and values are returned back to the main menu. Otherwise, an error message is printed and they also return values back to the main menu.

GUESSING NUMBER GAME CLASS

In this class, the game is created and the user can play the game if they wish.

In the __init__ method, the parent class inheritance takes place. All the attributes and methods from the parent class can be used. One variable outside of the inheritance is initialised. 

In the login_to_play() method, the user has to login using their details. If they cannot login successfully, an error message is printed to the screen and the logged_in value is set to 0, meaning that they are not logged in. Otherwise, a thank you meesage is printed and logged_in is set to 1 meaning that they are logged in. 

In the play_game() method, the functionality of the game is included here. It checks for whether the number of guesses is not equal to 0. If the user gets it right, a self.won variable value is incremented. Otherwise, a self.lost value is incremented. The number of rounds is incremented and many other variables are changed during the program. An example of a variable is the variable i. It can be set to 0 meaning the user lost the game or it can be set to 1 meaning they won.

The easy_level() method is run if the user picks to use the easy level. It receives the returned values from the play_game() method. With these values, it checks whether the user has enough wins to win a prize or not. If the user loses, they are sent back to the main menu. The number of wins and losses is always printed out after each round so that the user can see their result. 

The medium_level() method does basically the same thing as the easy_level() method. It receives the returned values from the play_game() method. With these values, it checks whether the user has enough wins to win a prize or not. If the user loses, they are sent back to the main menu. The number of wins and losses is always printed out after each round so that the user can see their result. 

The hard_level() method also does the similar thing. It receives the returned values from the play_game() method. With these values, it checks whether the user has enough wins to win a prize or not. If the user loses, they are sent back to the main menu. The number of wins and losses is always printed out after each round so that the user can see their result. 

ROCK PAPER SCISSORS CLASS

In this class, the user can play rock paper scissors.

In the __init__ method, attributes are inheritted from the parent class. Then, a variable that was not in the parent class is initialised. 

The login_to_play() methods checks the user so that they login before they play. If they have already logged in, they will be told that they cannot login. Otherwise, they will be asked to enter the email and password. If they match, the user will see a thank you message and the value of logged_in will be 1. Otherwise, an error message will appear and the logged_in value will be 0. 

The play_rock_paper_scissors() method checks all the possibilities that can happen if the user chooses an option. So, for instance, if the user chose rock and the computer chose scissors, the user would win. In this case, the user wins would be incremented by 1. If the computer won, the computer wins would be incremented by 1. If there is a draw, they draw variable would be incremented by 1. The rounds variable is always incremented to keep track of the round. The variable 'i' is used and can be of the value 0,1,2. If it is 0, the user lost. If it is 1, user won. If it is 2, it was a draw. These values are then returned to the play_the_game() method. 

The play_the_game() method keeps track of the result of the user in this game. First, the user enters the option out of the three (rock, paper or scissors). This is passed into the play_rock_paper_scissors() method. Once the values are returned from that method, they can be used in this method. If the user drew, the result would be updated and the draws would be incremented by 1. Same goes for if the user wins or loses. If the user won enough during the specified amount of rounds, they win a prize. Otherwise, they are returned back to the main menu. 

MENU

The menu function starts off with a while loop which will repeatedly run while j is 0. If j is 1, an inner loop will be run and it will allow the user to start the game they wish to play. Returning back to the j = 0 loop, there are many variables that are initialised to the values of either 0 or an empty string. Then, a create_account() method is called so that the user can create their account. Many values are returned from this function such as j, which tells the program whether the registration process went well. The user is then asked about the choice of game they wish to play. The first is passed to ensure the user is logged into the game. Once this is successful, the user can pick the level. Otherwise, they are returned back to the beginnning of the process. If the user chose to play rock paper scissors, the login_in_order_to_play() method is called. If the return value is 1, the play_the_game() method is called. Otherwise, an error message is printed. 
