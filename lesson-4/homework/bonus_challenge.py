import random

choices = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0

while player_score < 5 and computer_score < 5:
    player = input("rock, paper or scissors? ").lower()
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    
    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score => You: {player_score}, Computer: {computer_score}")

if player_score == 5:
    print("You won the match!")
else:
    print("Computer won the match!")