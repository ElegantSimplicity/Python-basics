# Rock Paper Scissor
# modified from
# thecleverprogrammer.com/2022/05/12/rock-paper-scissors-game-using-python/
import random

player = input('Please select Rock, Paper, or Scissor: ').lower()
computer = random.choice(['Rock', 'Paper', 'Scissor']).lower()
print('computer selected: ', computer)

if (player == 'rock'    and computer == 'paper')   or \
   (player == 'paper'   and computer == 'scissor') or \
   (player == 'scissor' and computer == 'rock'):
    print("computer WON")
elif player == computer:
    print("Tie")
else:
    print("player WON")