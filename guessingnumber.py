# This is a game where the user guesses the number
# if they guess correctly, the number of wins is increased by 1
# if they guess incorrectly, the number of losses is increased by 1
# The guessing number game has three levels: Easy, Medium and Hard. The user can pick whatever one
# The amount of wins and losses will be remembered.
# The user creates their own account which they use in this game
# The user must win a certain amount of rounds in order to win a prize. THe prize received is relative to the level chosen.
# The higher the level, the greater the prize.
import random

def create_user_account():
    # Registration
    print("Hello there!")
    name = input("Enter your name: ")
    email = input("Enter the email: ")
    password = input("Enter a password: ")
    print("Thank you " + name + "Now, you must enter your email and password to verify that everything is correct")

    email_input = input("Enter the email address you used: ")
    
    # This checks whether the email and password match the ones used at registration
    if email_input == email:
        print("Now, enter your password: ")
        your_pass = input()
        if your_pass == password:
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
        

def play_game(correct_number,guess,won,lost,rounds):
    i = 0
    while guess > 0:
        try:
            user_number = int(input("Guess the number: "))
        except ValueError:
            print("You have to enter a number!!! Try again: ")
        else:
            if user_number == correct_number:
                print("Correct!!!")
                won += 1
                guess = 0
                i = 1
                rounds += 1
                return won,i,rounds
            elif user_number < correct_number:
                guess -= 1
                if guess == 0:
                    print("You lost. The correct number was ",correct_number)
                    lost += 1
                    i = 0
                    rounds += 1
                    return lost,i,rounds
                else:
                    print("Higher!")
            elif user_number > correct_number:
                guess -= 1
                if guess == 0:
                    print("You lost. The correct number was ",correct_number)
                    lost += 1
                    i = 0
                    rounds += 1
                    return lost,i,rounds
                else:
                    print("Go lower!!!")

j = 0

while j == 0:
    j = create_user_account()
    game_difficulty = input("What game difficulty do you want to pick: Easy, Medium or Hard. Type the word in: ")
    no_of_wins = 0
    no_of_loss = 0
    no_of_rounds = 0
    while j == 1:

        if game_difficulty.startswith('e') or game_difficulty.startswith('E'):
            correct_number = random.randint(1,10)
            guess = 3
            correct_guesses,i,no_of_rounds = play_game(correct_number,guess,no_of_wins,no_of_loss,no_of_rounds)
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
            correct_guesses,i,no_of_rounds = play_game(correct_number,guess,no_of_wins,no_of_loss,no_of_rounds)
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
            correct_guesses,i,no_of_rounds = play_game(correct_number,guess,no_of_wins,no_of_loss,no_of_rounds)
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
