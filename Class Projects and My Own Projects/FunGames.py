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
    def __init__(self,name,email,password):
        # Initialising variables so that they can be used in the create_user_account() method
        self.name = name
        self.email = email
        self.password = password
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
                print("Thank you for logging in!!!")
                j = 1 # j is set to 1 so that the user does not need to create an account again
                return j # returns j
            else:
                print("Incorrect password")
                j = 0 # j is set to 0 meaning that the user must create the account again
                return j # returns j
        else:
            print("Incorrect email address")
            j = 0 # j is set to 0 so that the user has to create the account again
            return j # j is returned
    
class GuessingNumberGame(Games):
    def __init__(self,correct_number,guess,won,lost,rounds):
        # initialising variables to be used in method play_game()
        self.correct_number = correct_number
        self.guess = guess
        self.won = won
        self.lost = lost
        self.rounds = rounds
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
class RockPaperScissors(Games):
    def __init__(self,winnings,losses,draws,number_of_the_round,option_of_user):
        # initialise variables so that it can be used for play_rock_paper_scissors() method
        self.option_of_user = option_of_user
        self.winnings = winnings
        self.losses = losses
        self.draws = draws
        self.number_of_the_round = number_of_the_round
    def play_rock_paper_scissors(self):
        # this game allows the user to choose rock, paper or scissors and to see whether they can win and receive a prize
        computers_choice = random.choice(["Rock","Paper","Scissors"]) # randomises the computer's guess
        self.computers_choice = computers_choice 
        if self.computers_choice == "Rock" and self.option_of_user == "Rock": 
            print("No one wins!!")
            self.number_of_the_round += 1 # increase the round number by 1
            self.draws += 1 # increase draws by 1
            i = 2 # set i = 2 because this value will be returned and it goes inside the draws section in the menu()
            return self.draws,i,self.number_of_the_round # return values
        elif self.computers_choice == "Rock" and self.option_of_user == "Scissors":
            print("Computer wins!!")
            self.number_of_the_round += 1 # increase number of round by 1
            self.losses += 1 # increment losses
            i = 0 # set i = 0 because the user lost and this value will be returned.
            return self.losses,i,self.number_of_the_round
        elif self.computers_choice == "Rock" and self.option_of_user == "Paper":
            print("User wins!!!")
            self.number_of_the_round += 1 # increment round number by 1
            i = 1 # set i = 1 because user won
            self.winnings += 1 # increment winnings
            return self.winnings,i,self.number_of_the_round # return the values
        elif self.computers_choice == "Paper" and self.option_of_user == "Rock":
            print("Computer wins!!!")
            self.number_of_the_round += 1 # increment round number by 1
            self.losses += 1 # increment losses
            i = 0  # set i = 0 because the user lost and this value will be returned.
            return self.losses,i,self.number_of_the_round # return the values
        elif self.computers_choice == "Paper" and self.option_of_user == "Scissors":
            print("User wins!!!")
            self.number_of_the_round += 1 # increment round number by 1
            i = 1 # set i = 1 because user won
            self.winnings += 1 # increment winnings
            return self.winnings,i,self.number_of_the_round # return the values
        elif self.computers_choice == "Paper" and self.option_of_user == "Paper":
            print("No winners!!!")
            self.number_of_the_round += 1 # increment round number by 1
            self.draws += 1 # increment draws by 1
            i = 2 # set i = 2 because user drawed and this value will be returned to menu()
            return self.draws,i,self.number_of_the_round # return the values
        elif self.computers_choice == "Scissors" and self.option_of_user == "Scissors":
            print("No one won!!!")
            self.number_of_the_round += 1 # increment round number by 1
            self.draws += 1 # increment draws by 1
            i = 2 # set i = 2 because user drawed and this value will be returned to menu()
            return self.draws,i,self.number_of_the_round
        elif self.computers_choice == "Scissors" and self.option_of_user == "Paper":
            print("Computer wins!!!")
            self.number_of_the_round += 1 # increment round number by 1
            self.losses += 1 # increment losses by 1
            i = 0 # set i = 0 because user lost
            return self.losses,i,self.number_of_the_round # return values
        elif self.computers_choice == "Scissors" and self.option_of_user == "Rock":
            print("User wins!!!")
            self.number_of_the_round += 1 # increment round number by 1
            i = 1 # set i = 1 because user won
            self.winnings += 1 # increment winnings
            return self.winnings,i,self.number_of_the_round # return values
def menu():
    j = 0 

    while j == 0: # this loop is executed when the user needs to create an account. If they created it, this will not execute
                  # unless they finish the game and it will ask them to create a new account
        f_name = ''
        email_addr = ''
        pWord = ''
        j = Games(f_name,email_addr,pWord).create_user_account() # calls the Games class and the method inside it
        choice_of_game = input("Which game do you wish to play? GuessingNumberGame or RockPaperScissors?: ")
        if choice_of_game.startswith('g') or choice_of_game.startswith('G'):
            # if the user chose g or G, this game will be played.
            game_difficulty = input("What game difficulty do you want to pick: Easy, Medium or Hard. Type the word in: ")
            no_of_wins = 0
            no_of_loss = 0
            no_of_rounds = 0
            while j == 1: # this is executed if the value of j == 1. This loop lets the user play the game until
                          # they lose completely and then, they are prompted to create a new account
                if game_difficulty.startswith('e') or game_difficulty.startswith('E'):
                    # if the user chose the easy level/game
                    correct_number = random.randint(1,10) # random number from 1 to 10
                    guess = 3
                    correct_guesses,i,no_of_rounds = GuessingNumberGame(correct_number,guess,no_of_wins,no_of_loss,no_of_rounds).play_game()
                    if i == 1: # if the value returned from the method above is 1
                        no_of_wins = correct_guesses
                        if no_of_wins == 10 and no_of_rounds <= 12: # if the user won 10 times within 12 rounds
                            print("YOU WON A SPECIAL PRIZE: Samsung Galaxy A41")
                            print("Wins -> ",no_of_wins)
                            print("Loss -> ",no_of_loss)
                            j = 0
                        else: # if they didn't yet
                            print("Wins -> ",no_of_wins)
                            print("Loss -> ",no_of_loss)
                    elif i == 0: # if the value returned from the method above is 0
                        no_of_loss = correct_guesses
                        print("Wrong! You lost this round: ")
                        if no_of_wins < 10 and no_of_rounds > 12: # if the user won less than 10 in 12 rounds
                            print("You did not get 10 wins in 12 rounds. You lose: ")
                            j = 0
                        print("Wins -> ",no_of_wins)
                        print("Loss -> ",no_of_loss)
                elif game_difficulty.startswith('m') or game_difficulty.startswith('M'):
                    # this is if the user chooses the medium level of the game
                    correct_number = random.randint(1,30) # random number from 1 to 30
                    guess = 3
                    correct_guesses,i,no_of_rounds = GuessingNumberGame(correct_number,guess,no_of_wins,no_of_loss,no_of_rounds).play_game()
                    if i == 1: # if the value returned from the method above is 1
                        no_of_wins = correct_guesses
                        if no_of_wins == 12 and no_of_rounds <= 20: # if they won 12 times within 20 rounds
                            print("YOU WON A SPECIAL PRIZE: Huawei P30 Pro")
                            print("Wins -> ",no_of_wins)
                            print("Loss -> ",no_of_loss)
                            j = 0
                        else: # if they didn't yet
                            print("Wins -> ",no_of_wins)
                            print("Loss -> ",no_of_loss)
                    elif i == 0: # if the value returned from the method above is 0
                        no_of_loss = correct_guesses
                        print("Wrong! You lost this round: ")
                        if no_of_wins < 12 and no_of_rounds > 20: # if they won less than 12 times in 20 rounds
                            print("You did not get 12 wins in 20 rounds. You lose: ")
                            j = 0 # j is set to 0 because they must create a new account
                        print("Wins -> ",no_of_wins)
                        print("Loss -> ",no_of_loss)
                elif game_difficulty.startswith('h') or game_difficulty.startswith('H'):
                    # this is if the user chose the hard level of the game
                    correct_number = random.randint(1,100) # random number from 1 to 100
                    guess = 3
                    correct_guesses,i,no_of_rounds = GuessingNumberGame(correct_number,guess,no_of_wins,no_of_loss,no_of_rounds).play_game()
                    if i == 1: # if the value returned from the method above is 1
                        no_of_wins = correct_guesses
                        if no_of_wins == 16 and no_of_rounds <= 30: # if they won 16 times within 30 rounds
                            print("YOU WON A SPECIAL PRIZE: iPhone 12 Pro Max")
                            print("Wins -> ",no_of_wins)
                            print("Loss -> ",no_of_loss)
                            j = 0 # j = 0 meaning that the user has to create a new account because they won
                        else: # if they haven't yet
                            print("Wins -> ",no_of_wins)
                            print("Loss -> ",no_of_loss)
                    elif i == 0: # if the value returned from the method above is 0
                        no_of_loss = correct_guesses
                        print("Wrong! You lost this round: ")
                        if no_of_wins < 16 and no_of_rounds > 30: # if they won less than 16 times in 30 rounds
                            print("You did not get 16 wins in 30 rounds. You lose: ")
                            j = 0 # must create new account
                        print("Wins -> ",no_of_wins)
                        print("Loss -> ",no_of_loss)
                else: # if the user didn't choose either level
                    print("You must pick either Easy, Medium or Hard level: ")
        elif choice_of_game.startswith('r') or choice_of_game.startswith('R'):
            # if the user chooses to play the rock, paper or scissors game
            no_of_wins = 0
            no_of_loss = 0
            no_of_draws = 0
            no_of_rounds = 0
            while j == 1: # this loop will execute while j == 1. This means that the game will last until the value of j 
                          # switches to 0.
                l = 1 # this value is used so that it makes sure the user chooses either rock, paper or scissors.
                while l == 1: # loop that will run while the value is 1
                    user_option = input("Pick either rock, paper or scissors: ")
                    if user_option.startswith("R") or user_option.startswith("r"): # if rock is selected
                        user_option = "Rock" # set value to rock
                        l = 0 # l = 0 meaning that the loop will not execute anymore because the user chose the correct option
                    elif user_option.startswith("P") or user_option.startswith("p"): # if paper is selected
                        user_option = "Paper" # set value to paper
                        l = 0 # l = 0 meaning that the loop will not execute anymore because the user chose the correct option
                    elif user_option.startswith("S") or user_option.startswith("s"): # if scissors is selected
                        user_option = "Scissors" # set value to scissors
                        l = 0 # l = 0 meaning that the loop will not execute anymore because the user chose the correct option
                    else: # if none of the three options are selected
                        print("Wrong option selected. Try again")
                        l = 1 # loop value = 1 meaning that it must repeat again until the option is one of the three above
                    
                correct_attempts,i,no_of_rounds = RockPaperScissors(no_of_wins,no_of_loss,no_of_draws,no_of_rounds,user_option).play_rock_paper_scissors()
            
                if i == 2: # if the value returned from the above method is 2
                    no_of_draws = correct_attempts
                    print("You drew this round:")
                    print("Wins -> ",no_of_wins)
                    print("Loss -> ",no_of_loss)
                    print("Draws -> ",no_of_draws)
                    
                    if no_of_rounds > 10 and no_of_wins < 5: # if they get less than 5 wins within 10 rounds
                        print("You lost. You had to get 5 wins within 10 rounds. Try again: ")
                        j = 0 # must create an account again
                elif i == 1: # if the value returned from the above method is 1
                    no_of_wins = correct_attempts
                    if no_of_wins == 5 and no_of_rounds <= 10: # if they win 5 times within 10 rounds
                        print("YOU WON A PRIZE: CHOCOLATE BAR")
                        print("Wins -> ",no_of_wins)
                        print("Loss -> ",no_of_loss)
                        print("Draws -> ",no_of_draws)
                        j = 0 # must create an account again
                    elif no_of_wins <= 5 and no_of_rounds > 10: # if they win less than 5 times within 10 rounds
                        print("You didn't win within 10 rounds. Sorry: ")
                        print("Wins -> ",no_of_wins)
                        print("Loss -> ",no_of_loss)
                        print("Draws -> ",no_of_draws)
                        j = 0 # must create an account again
                    else:
                        print("Wins -> ",no_of_wins)
                        print("Loss -> ",no_of_loss)
                        print("Draws -> ",no_of_draws)
                elif i == 0: # if the value returned from the above method is 0
                    no_of_loss = correct_attempts
                    print("Wrong! You lost this round: ")
                    if no_of_wins < 5 and no_of_rounds > 10: # if they win less than 5 times within 10 rounds
                        print("You did not get 5 wins in 10 rounds. You lose: ")
                        j = 0 # must create an account again
                    print("Wins -> ",no_of_wins)
                    print("Loss -> ",no_of_loss)
                    print("Draws -> ",no_of_draws)
        else:
            print("You didn't select either game. You have to select either the guessing game (g) or the rock paper scissors game (r): ")
            j = 0 # must create an account again

menu() # menu() function is executed with this call
