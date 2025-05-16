import random

play = True
while play:
    number = random.randint(1, 100)
    attempts = 10
    while attempts > 0:
        guess = int(input("Guess a number (1-100): "))
        if guess == number:
            print("You guessed it right!")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")
        attempts -= 1
    if attempts == 0 and guess != number:
        print("You lost. Want to play again?")
        answer = input()
        if answer.lower() not in ['Y', 'YES', 'y', 'yes', 'ok']:
            play = False