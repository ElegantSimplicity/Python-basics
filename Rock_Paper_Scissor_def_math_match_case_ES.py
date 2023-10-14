def determine_winner(player, computer):
    # a nice expression from https://stackoverflow.com/a/2795421/10503796
    winner = (player - computer + 3) % 3
    match winner:
        case 0: return 'TIE'
        case 1: return 'Player WON'
        case 2: return 'Computer WON'

import random
convention = {0 : 'Rock', 1 : 'Paper', 2 : 'Scissors'}
player = int(input('Please select 0 for Rock, 1 for Paper, 2 for Scissors: '))
computer = random.choice([0, 1, 2])
print(f'You selected: {convention[player]} \nComputer selected: {convention[computer]}')
print(determine_winner(player, computer))