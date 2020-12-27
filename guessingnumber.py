# This is a game where the user guesses the number and if they guess correctly, they get a prize and if they guess incorrectly, they can guess again
# The guessing number game has three levels: Easy, Medium and Hard. The user can pick whatever one
# The amount of wins and losses will be remembered.
import random

def play_game(correct_number,guess,won,lost):
    i = 0
    while guess > 0:
        try:
            user_number = int(input("Guess the number: "))
        except ValueError:
            print("You have to enter a number!!! Try again: ")
        else:
            if user_number == correct_number:
                print("Correct!!! You won a prize!!")
                won += 1
                guess = 0
                i = 1
                return won,i
            elif user_number < correct_number:
                guess -= 1
                if guess == 0:
                    print("You lost. The correct number was ",correct_number)
                    lost += 1
                    i = 0
                    return lost,i
                else:
                    print("Higher!")
            elif user_number > correct_number:
                guess -= 1
                if guess == 0:
                    print("You lost. The correct number was ",correct_number)
                    lost += 1
                    i = 0
                    return lost,i
                else:
                    print("Go lower!!!")

no_of_wins = 0
no_of_loss = 0

while True:
    game_difficulty = input("What game difficulty do you want to pick: Easy, Medium or Hard. Type the word in: ")

    if game_difficulty.startswith('e') or game_difficulty.startswith('E'):
        correct_number = random.randint(1,10)
        print(correct_number)
        guess = 3
        correct_guesses,i = play_game(correct_number,guess,no_of_wins,no_of_loss)
        if i == 1:
            no_of_wins = correct_guesses
            print("Wins -> ",no_of_wins)
            print("Loss -> ",no_of_loss)
        elif i == 0:
            no_of_loss = correct_guesses
            print("Wins -> ",no_of_wins)
            print("Loss -> ",no_of_loss)
    elif game_difficulty.startswith('m') or game_difficulty.startswith('M'):
        correct_number = random.randint(1,30)
        print(correct_number)
        guess = 3
        correct_guesses,i = play_game(correct_number,guess,no_of_wins,no_of_loss)
        if i == 1:
            no_of_wins = correct_guesses
            print("Wins -> ",no_of_wins)
            print("Loss -> ",no_of_loss)
        elif i == 0:
            no_of_loss = correct_guesses
            print("Wins -> ",no_of_wins)
            print("Loss -> ",no_of_loss)
    elif game_difficulty.startswith('h') or game_difficulty.startswith('H'):
        correct_number = random.randint(1,100)
        print(correct_number)
        guess = 3
        correct_guesses,i = play_game(correct_number,guess,no_of_wins,no_of_loss)
        if i == 1:
            no_of_wins = correct_guesses
            print("Wins -> ",no_of_wins)
            print("Loss -> ",no_of_loss)
        elif i == 0:
            no_of_loss = correct_guesses
            print("Wins -> ",no_of_wins)
            print("Loss -> ",no_of_loss)
    else:
        print("You must pick either Easy, Medium or Hard level: ")
