# Rock Paper Scissor (by Le Huy Tien)
# based on a nice idea of the winner expresion from
# https://stackoverflow.com/a/2795421/10503796
# I use dict and match case
import random
convention= {0 : 'Rock', 1 : 'Paper', 2 : 'Scissors'}
print(convention)
player = int(input('Please select: '))
computer = random.choice([0,1,2])
print(f'You selected: {convention[player]}')
print(f'Computer selected: {convention[computer]}')

winner = (3 + player - computer) % 3

match winner:
    case 0: print('TIE')
    case 1: print('player WON')
    case 2: print('computer WON')