# Author -> Amar Plakalo
# There are two available games to be played: Guessing number game and Rock, Paper, Scissors.
# *****************GUESSING GAME*****************
# This is a game where the user guesses the number
# if they guess correctly, the number of wins is increased by 1
# if they guess incorrectly, the number of losses is increased by 1
# The guessing number game has three levels: Easy, Medium and Hard. The user can pick whatever one
# The amount of wins and losses will be remembered.
# The user creates their own account which they use in this game
# The user must win a certain amount of rounds in order to win a prize. THe prize received is relative to the level chosen.
# The higher the level, the greater the prize.
# *****************ROCK PAPER SCISSORS*****************
# The user creates their own account which they use in this game
# The user plays against the computer.
# The user picks whether they will use rock, paper or scissors
# If the user wins the round, the number of wins they accumulated will increase
# If the computer wins, the user's losses will increase
# If they draw, the user will have the draws increased
# If the user wins, they will receive a prize.
import random

class Games(object):
    def __init__(self,name,email,password,guess,won,lost,rounds):
        # Initialising variables so that they can be used
        self.name = name
        self.email = email
        self.password = password
        self.guess = guess
        self.won = won
        self.lost = lost
        self.rounds = rounds
    def create_user_account(self):
        # Registration
        print("Hello there!")
        self.name = input("Enter your name: ")
        self.email = input("Enter the email: ")
        self.password = input("Enter a password: ")
        print("Thank you " + self.name + "Now, you must enter your email and password to verify that everything is correct")

        email_input = input("Enter the email address you used: ")
    
        # This checks whether the email and password match the ones used at registration
        if email_input == self.email:
            print("Now, enter your password: ")
            your_pass = input() 
            if your_pass == self.password: # if the password entered is equal to the password that was set
                print("Thanks for verifying your account!")
                j = 1 # j is set to 1 so that the user does not need to create an account again
                return j,self.name,self.email,self.password # returns j
            else:
                print("Incorrect password")
                j = 0 # j is set to 0 meaning that the user must create the account again
                return j,self.name,self.email,self.password # returns j
        else:
            print("Incorrect email address")
            j = 0 # j is set to 0 so that the user has to create the account again
            return j,self.name,self.email,self.password # j is returned
class GuessingNumberGame(Games):
    def __init__(self,name,email,password,guess,won,lost,rounds,correct_number):
        Games.__init__(self,name,email,password,guess,won,lost,rounds)
        # initialising variables to be used in method play_game()
        self.correct_number = correct_number
    def login_to_play(self,logged_in):
        # this method will allow the user to login and it will open a file for the user so that his/her records will be saved
        print("Hello " + self.name + ".Can you enter your email and password in order to login? ")
        email_entered = input("Enter email: ")
        pass_entered = input("Enter password: ")

        if email_entered == self.email and pass_entered == self.password:
            print("You have logged in!")
            logged_in = 1
            return logged_in
        elif email_entered != self.email and pass_entered != self.password:
            print("Incorrect email AND password: ")
            logged_in = 0
            return logged_in
        elif email_entered == self.email and pass_entered != self.password:
            print("Password entered is NOT correct: ")
            logged_in = 0
            return logged_in
        elif email_entered != self.email and pass_entered == self.password:
            print("Email entered is not correct: ")
            logged_in = 0
            return logged_in

    def play_game(self):
        # this method lets the user play the guessing game by guessing a number and seeing whether
        # the number guessed == to the number that was given.
        i = 0 
        while self.guess > 0: # while the user has more than 0 guesses
            try: # attempt to do this
                user_number = int(input("Guess the number: ")) # enter a number
            except ValueError: # expect a value error because a number was not entered
                print("You have to enter a number!!! Try again: ")
            else: # in the case that a number was entered
                if user_number == self.correct_number: # if the number guessed is equal to the number given
                    print("Correct!!!")
                    self.won += 1 # increment wins
                    self.guess = 0 # set guess value to 0
                    i = 1 # set i = 1 so that it can be returned back. i = 1 means that the user won 
                    self.rounds += 1 # increment the round number
                    return self.won,i,self.rounds # return all the values
                elif user_number < self.correct_number: # if the guessed number less than given number
                    self.guess -= 1 # decrement the guess count because they have three attempts to guess that number
                    if self.guess == 0: # if the guess count is 0
                        print("You lost. The correct number was ",self.correct_number)
                        self.lost += 1 # increment losses
                        i = 0 # set i to 0
                        self.rounds += 1 # increment the round number
                        return self.lost,i,self.rounds # return values
                    else: # if there is more than 0 guesses left
                        print("Higher!")
                elif user_number > self.correct_number:
                    self.guess -= 1 # decrement the guess count because they have three attempts to guess that number
                    if self.guess == 0: # if the guess count is 0
                        print("You lost. The correct number was ",self.correct_number)
                        self.lost += 1 # increment losses
                        i = 0 # set i to 0
                        self.rounds += 1 # increment i by 1
                        return self.lost,i,self.rounds # return values
                    else: # if there is more than 0 guesses left
                        print("Go lower!!!")
    def easy_level(self,j):
        while j == 1:
            # if the user chose the easy level/game
            self.correct_number = random.randint(1,10) # random number from 1 to 10
            guess = 3
            correct_guesses,i,self.rounds = GuessingNumberGame(self.name,self.email,self.password,guess,self.won,self.lost,self.rounds,self.correct_number).play_game()
            if i == 1: # if the value returned from the method above is 1
                self.won = correct_guesses
                if self.won == 10 and self.rounds <= 12: # if the user won 10 times within 12 rounds
                    print("YOU WON A SPECIAL PRIZE: Samsung Galaxy A41")
                    print("Wins -> ",self.won)
                    print("Loss -> ",self.lost)
                    j = 0
                    menu()
                elif self.won <= 10 and self.rounds > 12:
                    print("You failed to win within 12 rounds: ")
                    j = 0
                    menu()
                else: # if they didn't yet
                    print("Wins -> ",self.won)
                    print("Loss -> ",self.lost)
            elif i == 0: # if the value returned from the method above is 0

                print("Wrong! You lost this round: ")
                self.lost = correct_guesses
                if self.won < 10 and self.rounds > 12: # if the user won less than 10 in 12 rounds
                    print("You did not get 10 wins in 12 rounds. You lose: ")
                    j = 0
                    menu()
                print("Wins -> ",self.won)
                print("Loss -> ",self.lost)

    def medium_level(self,j):
        while j == 1:
            self.correct_number = random.randint(1,30) # random number from 1 to 30
            guess = 3
            correct_guesses,i,self.rounds = GuessingNumberGame(self.name,self.email,self.password,guess,self.won,self.lost,self.rounds,self.correct_number).play_game()
            if i == 1: # if the value returned from the method above is 1
                self.won = correct_guesses
                if self.won == 12 and self.rounds <= 20: # if they won 12 times within 20 rounds
                    print("YOU WON A SPECIAL PRIZE: Huawei P30 Pro")
                    print("Wins -> ",self.won)
                    print("Loss -> ",self.lost)
                    j = 0
                    menu()
                elif self.won <= 12 and self.rounds > 20:
                    print("You have not won 12 times within 20 rounds: ")
                    j = 0
                    menu()
                else: # if they didn't yet
                    print("Wins -> ",self.won)
                    print("Loss -> ",self.lost)
            elif i == 0: # if the value returned from the method above is 0
                print("Wrong! You lost this round: ")
                self.lost = correct_guesses
                if self.won < 12 and self.rounds > 20: # if they won less than 12 times in 20 rounds
                    print("You did not get 12 wins in 20 rounds. You lose: ")
                    j = 0 # j is set to 0 because they must create a new account
                    menu()
                print("Wins -> ",self.won)
                print("Loss -> ",self.lost)
    def hard_level(self,j):
        while j == 1:
            self.correct_number = random.randint(1,100) # random number from 1 to 100
            guess = 3
            correct_guesses,i,self.rounds = GuessingNumberGame(self.name,self.email,self.password,guess,self.won,self.lost,self.rounds,self.correct_number).play_game()
            if i == 1: # if the value returned from the method above is 1
                self.won = correct_guesses
                if self.won == 16 and self.rounds <= 30: # if they won 16 times within 30 rounds
                    print("YOU WON A SPECIAL PRIZE: iPhone 12 Pro Max")
                    print("Wins -> ",self.won)
                    print("Loss -> ",self.lost)
                    j = 0 # j = 0 meaning that the user has to create a new account because they won
                    menu()
                elif self.won <= 16 and self.rounds > 30:
                    print("You have not won 16 times within 30 rounds: ")
                    j = 0
                    menu()
                else: # if they haven't yet
                    print("Wins -> ",self.won)
                    print("Loss -> ",self.rounds)
            elif i == 0: # if the value returned from the method above is 0
                print("Wrong! You lost this round: ")
                self.lost = correct_guesses
                if self.won < 16 and self.rounds > 30: # if they won less than 16 times in 30 rounds
                    print("You did not get 16 wins in 30 rounds. You lose: ")
                    j = 0 # must create new account
                    menu()
                print("Wins -> ",self.won)
                print("Loss -> ",self.lost)
class RockPaperScissors(Games):
    def __init__(self,name,email,password,guess,won,lost,rounds,draws):
        Games.__init__(self,name,email,password,guess,won,lost,rounds)
        # initialise variables so that it can be used for play_rock_paper_scissors() method
        self.draws = draws
    def login_in_order_to_play(self,logged_in):
        if logged_in == 1:
            print("You are already logged in - you cannot login when you are logged in: ")
        elif logged_in == 0:
            print("Hello " + self.name + ".Can you enter your email and password in order to login? ")
            email_entered = input("Enter email: ")
            pass_entered = input("Enter password: ")

            if email_entered == self.email and pass_entered == self.password:
                print("You have logged in!")
                logged_in = 1
                return logged_in
            elif email_entered != self.email and pass_entered != self.password:
                print("Incorrect email AND password: ")
                logged_in = 0
                return logged_in
            elif email_entered == self.email and pass_entered != self.password:
                print("Password entered is NOT correct: ")
                logged_in = 0
                return logged_in
            elif email_entered != self.email and pass_entered == self.password:
                print("Email entered is not correct: ")
                logged_in = 0
                return logged_in
        
    def play_rock_paper_scissors(self,option_of_user):
        # this game allows the user to choose rock, paper or scissors and to see whether they can win and receive a prize
        computers_choice = random.choice(["Rock","Paper","Scissors"]) # randomises the computer's guess
        self.computers_choice = computers_choice 
        if self.computers_choice == "Rock" and option_of_user == "Rock": 
            print("No one wins!!")
            self.rounds += 1 # increase the round number by 1
            self.draws += 1 # increase draws by 1
            i = 2 # set i = 2 because this value will be returned and it goes inside the draws section in the menu()
            
            return self.draws,i,self.rounds
        elif self.computers_choice == "Rock" and option_of_user == "Scissors":
            print("Computer wins!!")
            self.rounds += 1 # increase number of round by 1
            self.lost += 1 # increment losses
            i = 0 # set i = 0 because the user lost and this value will be returned.
            
            return self.lost,i,self.rounds
        elif self.computers_choice == "Rock" and option_of_user == "Paper":
            print("User wins!!!")
            self.rounds += 1 # increment round number by 1
            i = 1 # set i = 1 because user won
            self.won += 1 # increment winnings
            return self.won,i,self.rounds
        elif self.computers_choice == "Paper" and option_of_user == "Rock":
            print("Computer wins!!!")
            self.rounds += 1 # increment round number by 1
            self.lost += 1 # increment losses
            i = 0  # set i = 0 because the user lost and this value will be returned.
            return self.lost,i,self.rounds
        elif self.computers_choice == "Paper" and option_of_user == "Scissors":
            print("User wins!!!")
            self.rounds += 1 # increment round number by 1
            i = 1 # set i = 1 because user won
            self.won += 1 # increment winnings
            return self.won,i,self.rounds
        elif self.computers_choice == "Paper" and option_of_user == "Paper":
            print("No winners!!!")
            self.rounds += 1 # increment round number by 1
            self.draws += 1 # increment draws by 1
            i = 2 # set i = 2 because user drawed and this value will be returned to menu()
            return self.draws,i,self.rounds
        elif self.computers_choice == "Scissors" and option_of_user == "Scissors":
            print("No one won!!!")
            self.rounds += 1 # increment round number by 1
            self.draws += 1 # increment draws by 1
            i = 2 # set i = 2 because user drawed and this value will be returned to menu()
            return self.draws,i,self.rounds
        elif self.computers_choice == "Scissors" and option_of_user == "Paper":
            print("Computer wins!!!")
            self.rounds += 1 # increment round number by 1
            self.lost += 1 # increment losses by 1
            i = 0 # set i = 0 because user lost
            return self.lost,i,self.rounds
        elif self.computers_choice == "Scissors" and option_of_user == "Rock":
            print("User wins!!!")
            self.rounds += 1 # increment round number by 1
            i = 1 # set i = 1 because user won
            self.won += 1 # increment winnings
            return self.won,i,self.rounds
    def play_the_game(self):
        j = 1
        while j == 1:

            user_option = input("Pick either rock, paper or scissors: ")
            if user_option.startswith("R") or user_option.startswith("r"): # if rock is selected
                user_option = "Rock" # set value to rock
            elif user_option.startswith("P") or user_option.startswith("p"): # if paper is selected
                user_option = "Paper" # set value to paper
            elif user_option.startswith("S") or user_option.startswith("s"): # if scissors is selected
                user_option = "Scissors" # set value to scissors
            else: # if none of the three options are selected
                print("Wrong option selected. Try again")

            correct_attempts,i,self.rounds = RockPaperScissors(self.name,self.email,self.password,self.guess,self.won,self.lost,self.rounds,self.draws).play_rock_paper_scissors(user_option)
            if i == 2:
                self.draws = correct_attempts
                print("You drew this round:")
                print("Wins -> ",self.won)
                print("Loss -> ",self.lost)
                print("Draws -> ",self.draws)
                j = 1
                
                if self.rounds > 10 and self.won < 5: # if they get less than 5 wins within 10 rounds
                    print("You lost. You had to get 5 wins within 10 rounds. Try again: ")
                    j = 0
                    menu()
            elif i == 1: # if the value returned from the above method is 1
                self.won = correct_attempts
                if self.won == 5 and self.rounds <= 10: # if they win 5 times within 10 rounds
                    print("YOU WON A PRIZE: CHOCOLATE BAR")
                    print("Wins -> ",self.won)
                    print("Loss -> ",self.lost)
                    print("Draws -> ",self.draws)
                    j = 0
                    menu()
                elif self.won <= 5 and self.rounds > 10: # if they win less than 5 times within 10 rounds
                    print("You didn't win within 10 rounds. Sorry: ")
                    print("Wins -> ",self.won)
                    print("Loss -> ",self.lost)
                    print("Draws -> ",self.draws)
                    j = 0
                    menu()
                  
                else:
                    print("Wins -> ",self.won)
                    print("Loss -> ",self.lost)
                    print("Draws -> ",self.draws)
                    j = 1
            elif i == 0: # if the value returned from the above method is 0
                self.lost = correct_attempts
                print("Wrong! You lost this round: ")
                if self.won < 5 and self.rounds > 10: # if they win less than 5 times within 10 rounds
                    print("You did not get 5 wins in 10 rounds. You lose: ")
                    j = 0
                    menu()
                print("Wins -> ",self.won)
                print("Loss -> ",self.lost)
                print("Draws -> ",self.draws)
                j = 1
def menu():
    j = 0

    while j == 0: # this loop is executed when the user needs to create an account. If they created it, this will not execute
                  # unless they finish the game and it will ask them to create a new account
        f_name = ''
        email_addr = ''
        pWord = ''
        logged_in = 0 
        no_of_wins = 0
        no_of_loss = 0
        no_of_draws = 0
        no_of_rounds = 0
        correct_number = 0
        guess = 0
        j,f_name,email_addr,pWord = Games(f_name,email_addr,pWord,guess,no_of_wins,no_of_loss,no_of_rounds).create_user_account() # calls the Games class and the method inside it

        choice_of_game = input("Which game do you wish to play? GuessingNumberGame or RockPaperScissors?: ")
        if choice_of_game.startswith('g') or choice_of_game.startswith('G'):
            # if the user chose g or G, this game will be played.
            logged_in = GuessingNumberGame(f_name,email_addr,pWord,correct_number,guess,no_of_wins,no_of_loss,no_of_rounds).login_to_play(logged_in)
            if logged_in == 1:
                game_difficulty = input("What game difficulty do you want to pick: Easy, Medium or Hard. Type the word in: ")
                while j == 1: # this is executed if the value of j == 1. This loop lets the user play the game until
                            # they lose completely and then, they are prompted to create a new account
                    if game_difficulty.startswith('e') or game_difficulty.startswith('E'):
                        GuessingNumberGame(f_name,email_addr,pWord,correct_number,guess,no_of_wins,no_of_loss,no_of_rounds).easy_level(j)
                    
                    elif game_difficulty.startswith('m') or game_difficulty.startswith('M'):
                        # this is if the user chooses the medium level of the game
                        GuessingNumberGame(f_name,email_addr,pWord,correct_number,guess,no_of_wins,no_of_loss,no_of_rounds).medium_level(j)
                    elif game_difficulty.startswith('h') or game_difficulty.startswith('H'):
                        # this is if the user chose the hard level of the game
                        GuessingNumberGame(f_name,email_addr,pWord,correct_number,guess,no_of_wins,no_of_loss,no_of_rounds).hard_level(j)
                    else: # if the user didn't choose either level
                        print("You must pick either Easy, Medium or Hard level: ")
            elif logged_in == 0:
                print("You didn't login - you cannot play: ")
                j = 0
        elif choice_of_game.startswith('r') or choice_of_game.startswith('R'):
            logged_in = RockPaperScissors(f_name,email_addr,pWord,guess,no_of_wins,no_of_loss,no_of_rounds,no_of_draws).login_in_order_to_play(logged_in)
            if logged_in == 1:
                RockPaperScissors(f_name,email_addr,pWord,guess,no_of_wins,no_of_loss,no_of_rounds,no_of_draws).play_the_game()
            elif logged_in == 0:
                print("You are not logged in - you cannot play the game: ")


menu() # menu() function is executed with this call
