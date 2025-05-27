import random


def playerGuess():
    player_guess = input(
        "I'm thinking of a nuumber between 1-100! Can you guess it? ")
    while True:
        if player_guess.isdigit() and int(player_guess) > 1 and int(player_guess) < 100:
            return int(player_guess)
        else:
            player_guess = input(
                "Please enter a valid number between 1 and 100: ")


def playerRetry():
    player_guess = input(
        "Your answer was incorrect, Guess Again: ")
    while True:
        if player_guess.isdigit() and int(player_guess) > 1 and int(player_guess) < 100:
            return int(player_guess)
        else:
            player_guess = input(
                "Please enter a valid number between 1 and 100: ")


def computerAnswer():
    computer_answer = random.randint(1, 100)
    return computer_answer


def checkAnswer(player_guess, computer_answer):

    while True:
        if player_guess < computer_answer:
            print("Answer to Low!")
            player_guess = playerRetry()
        elif player_guess > computer_answer:
            print("Answer to High!")
            player_guess = playerRetry()
        else:
            return f"Computer Guess was: {computer_answer}! You were correct!"


while True:
    player_guess = playerGuess()
    computer_answer = computerAnswer()
    print(checkAnswer(player_guess, computer_answer))

    continue_game = input("Would you like to play again? (y/n) ")

    if continue_game.lower() == "n":
        break

print("Thank you for playing! Coming Again Soon!")
