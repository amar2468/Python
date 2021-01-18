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
            if your_pass == self.password:
                print("Thank you for logging in!!!")
                j = 1
                return j
            else:
                print("Incorrect password")
                j = 0
                return j
        else:
            print("Incorrect email address")
            j = 0
            return j
    
class GuessingNumberGame(Games):
    def __init__(self,correct_number,guess,won,lost,rounds):
        self.correct_number = correct_number
        self.guess = guess
        self.won = won
        self.lost = lost
        self.rounds = rounds
    def play_game(self):
        i = 0
        while self.guess > 0:
            try:
                user_number = int(input("Guess the number: "))
            except ValueError:
                print("You have to enter a number!!! Try again: ")
            else:
                if user_number == self.correct_number:
                    print("Correct!!!")
                    self.won += 1
                    self.guess = 0
                    i = 1
                    self.rounds += 1
                    return self.won,i,self.rounds
                elif user_number < self.correct_number:
                    self.guess -= 1
                    if self.guess == 0:
                        print("You lost. The correct number was ",self.correct_number)
                        self.lost += 1
                        i = 0
                        self.rounds += 1
                        return self.lost,i,self.rounds
                    else:
                        print("Higher!")
                elif user_number > self.correct_number:
                    self.guess -= 1
                    if self.guess == 0:
                        print("You lost. The correct number was ",self.correct_number)
                        self.lost += 1
                        i = 0
                        self.rounds += 1
                        return self.lost,i,self.rounds
                    else:
                        print("Go lower!!!")
class RockPaperScissors(Games):
    def __init__(self,winnings,losses,draws,number_of_the_round,option_of_user):
        self.option_of_user = option_of_user
        self.winnings = winnings
        self.losses = losses
        self.draws = draws
        self.number_of_the_round = number_of_the_round
    def play_rock_paper_scissors(self):
        computers_choice = random.choice(["Rock","Paper","Scissors"])
        self.computers_choice = computers_choice
        if self.computers_choice == "Rock" and self.option_of_user == "Rock":
            print("No one wins!!")
            self.number_of_the_round += 1
            self.draws += 1
            i = 2
            return self.draws,i,self.number_of_the_round
        elif self.computers_choice == "Rock" and self.option_of_user == "Scissors":
            print("Computer wins!!")
            self.number_of_the_round += 1
            self.losses += 1
            i = 0
            return self.losses,i,self.number_of_the_round
        elif self.computers_choice == "Rock" and self.option_of_user == "Paper":
            print("User wins!!!")
            self.number_of_the_round += 1
            i = 1
            self.winnings += 1
            return self.winnings,i,self.number_of_the_round
        elif self.computers_choice == "Paper" and self.option_of_user == "Rock":
            print("Computer wins!!!")
            self.number_of_the_round += 1
            self.losses += 1
            i = 0
            return self.losses,i,self.number_of_the_round
        elif self.computers_choice == "Paper" and self.option_of_user == "Scissors":
            print("User wins!!!")
            self.number_of_the_round += 1
            i = 1
            self.winnings += 1
            return self.winnings,i,self.number_of_the_round
        elif self.computers_choice == "Paper" and self.option_of_user == "Paper":
            print("No winners!!!")
            self.number_of_the_round += 1
            self.draws += 1
            i = 2
            return self.draws,i,self.number_of_the_round
        elif self.computers_choice == "Scissors" and self.option_of_user == "Scissors":
            print("No one won!!!")
            self.number_of_the_round += 1
            self.draws += 1
            i = 2
            return self.draws,i,self.number_of_the_round
        elif self.computers_choice == "Scissors" and self.option_of_user == "Paper":
            print("Computer wins!!!")
            self.number_of_the_round += 1
            self.losses += 1
            i = 0
            return self.losses,i,self.number_of_the_round
        elif self.computers_choice == "Scissors" and self.option_of_user == "Rock":
            print("User wins!!!")
            self.number_of_the_round += 1
            i = 1
            self.winnings += 1
            return self.winnings,i,self.number_of_the_round
def menu():
    j = 0

    while j == 0:
        f_name = ''
        email_addr = ''
        pWord = ''
        j = Games(f_name,email_addr,pWord).create_user_account()
        choice_of_game = input("Which game do you wish to play? GuessingNumberGame or RockPaperScissors?: ")
        if choice_of_game.startswith('g') or choice_of_game.startswith('G'):

            game_difficulty = input("What game difficulty do you want to pick: Easy, Medium or Hard. Type the word in: ")
            no_of_wins = 0
            no_of_loss = 0
            no_of_rounds = 0
            while j == 1:

                if game_difficulty.startswith('e') or game_difficulty.startswith('E'):
                    correct_number = random.randint(1,10)
                    guess = 3
                    correct_guesses,i,no_of_rounds = GuessingNumberGame(correct_number,guess,no_of_wins,no_of_loss,no_of_rounds).play_game()
                    if i == 1:
                        no_of_wins = correct_guesses
                        if no_of_wins == 10 and no_of_rounds <= 12:
                            print("YOU WON A SPECIAL PRIZE: Samsung Galaxy A41")
                            print("Wins -> ",no_of_wins)
                            print("Loss -> ",no_of_loss)
                            j = 0
                        else:
                            print("Wins -> ",no_of_wins)
                            print("Loss -> ",no_of_loss)
                    elif i == 0:
                        no_of_loss = correct_guesses
                        print("Wrong! You lost this round: ")
                        if no_of_wins < 10 and no_of_rounds > 12:
                            print("You did not get 10 wins in 12 rounds. You lose: ")
                            j = 0
                        print("Wins -> ",no_of_wins)
                        print("Loss -> ",no_of_loss)
                elif game_difficulty.startswith('m') or game_difficulty.startswith('M'):
                    correct_number = random.randint(1,30)
                    guess = 3
                    correct_guesses,i,no_of_rounds = GuessingNumberGame(correct_number,guess,no_of_wins,no_of_loss,no_of_rounds).play_game()
                    if i == 1:
                        no_of_wins = correct_guesses
                        if no_of_wins == 12 and no_of_rounds <= 20:
                            print("YOU WON A SPECIAL PRIZE: Huawei P30 Pro")
                            print("Wins -> ",no_of_wins)
                            print("Loss -> ",no_of_loss)
                            j = 0
                        else:
                            print("Wins -> ",no_of_wins)
                            print("Loss -> ",no_of_loss)
                    elif i == 0:
                        no_of_loss = correct_guesses
                        print("Wrong! You lost this round: ")
                        if no_of_wins < 12 and no_of_rounds > 20:
                            print("You did not get 12 wins in 20 rounds. You lose: ")
                            j = 0
                        print("Wins -> ",no_of_wins)
                        print("Loss -> ",no_of_loss)
                elif game_difficulty.startswith('h') or game_difficulty.startswith('H'):
                    correct_number = random.randint(1,100)
                    guess = 3
                    correct_guesses,i,no_of_rounds = GuessingNumberGame(correct_number,guess,no_of_wins,no_of_loss,no_of_rounds).play_game()
                    if i == 1:
                        no_of_wins = correct_guesses
                        if no_of_wins == 16 and no_of_rounds <= 30:
                            print("YOU WON A SPECIAL PRIZE: iPhone 12 Pro Max")
                            print("Wins -> ",no_of_wins)
                            print("Loss -> ",no_of_loss)
                            j = 0
                        else:
                            print("Wins -> ",no_of_wins)
                            print("Loss -> ",no_of_loss)
                    elif i == 0:
                        no_of_loss = correct_guesses
                        print("Wrong! You lost this round: ")
                        if no_of_wins < 16 and no_of_rounds > 30:
                            print("You did not get 16 wins in 30 rounds. You lose: ")
                            j = 0
                        print("Wins -> ",no_of_wins)
                        print("Loss -> ",no_of_loss)
                else:
                    print("You must pick either Easy, Medium or Hard level: ")
        elif choice_of_game.startswith('r') or choice_of_game.startswith('R'):
            no_of_wins = 0
            no_of_loss = 0
            no_of_draws = 0
            no_of_rounds = 0
            while j == 1:
                l = 1
                while l == 1:
                    user_option = input("Pick either rock, paper or scissors: ")
                    if user_option.startswith("R") or user_option.startswith("r"):
                        user_option = "Rock"
                        l = 0
                    elif user_option.startswith("P") or user_option.startswith("p"):
                        user_option = "Paper"
                        l = 0
                    elif user_option.startswith("S") or user_option.startswith("s"):
                        user_option = "Scissors"
                        l = 0
                    else:
                        print("Wrong option selected. Try again")
                        l = 1
                    
                correct_attempts,i,no_of_rounds = RockPaperScissors(no_of_wins,no_of_loss,no_of_draws,no_of_rounds,user_option).play_rock_paper_scissors()
            
                if i == 2:
                    no_of_draws = correct_attempts
                    print("You drew this round:")
                    print("Wins -> ",no_of_wins)
                    print("Loss -> ",no_of_loss)
                    print("Draws -> ",no_of_draws)
                    
                    if no_of_rounds > 10 and no_of_wins < 5:
                        print("You lost. You had to get 5 wins within 10 rounds. Try again: ")
                        j = 0
                elif i == 1:
                    no_of_wins = correct_attempts
                    if no_of_wins == 5 and no_of_rounds <= 10:
                        print("YOU WON A PRIZE: CHOCOLATE BAR")
                        print("Wins -> ",no_of_wins)
                        print("Loss -> ",no_of_loss)
                        print("Draws -> ",no_of_draws)
                        j = 0
                    elif no_of_wins <= 5 and no_of_rounds > 10:
                        print("You didn't win within 10 rounds. Sorry: ")
                        print("Wins -> ",no_of_wins)
                        print("Loss -> ",no_of_loss)
                        print("Draws -> ",no_of_draws)
                        j = 0
                    else:
                        print("Wins -> ",no_of_wins)
                        print("Loss -> ",no_of_loss)
                        print("Draws -> ",no_of_draws)
                elif i == 0:
                    no_of_loss = correct_attempts
                    print("Wrong! You lost this round: ")
                    if no_of_wins < 5 and no_of_rounds > 10:
                        print("You did not get 5 wins in 10 rounds. You lose: ")
                        j = 0
                    print("Wins -> ",no_of_wins)
                    print("Loss -> ",no_of_loss)
                    print("Draws -> ",no_of_draws)
        else:
            print("You didn't select either game. You have to select either the guessing game (g) or the rock paper scissors game (r): ")
            j = 0

menu()
