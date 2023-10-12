# Rock Paper Scissor
import random

player = input('Please select Rock, Paper, or Scissors: ').lower()
computer = random.choice(['Rock', 'Paper', 'Scissors']).lower()
print('computer selected: ', computer)

if (player,computer) in {('rock','paper'),('paper','scissors'),('scissors','rock')}:
    print("computer WON")
elif player == computer: print("Tie")
else: print("player WON")