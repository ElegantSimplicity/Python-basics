def determine_winner(player, computer):
    winner = (3 + player - computer) % 3
    match winner:
        case 0: return 'TIE'
        case 1: return 'Player WON'
        case 2: return 'Computer WON'

import random
print('Welcome to Rock, Paper, Scissors!')
convention={0 : 'Rock', 1 : 'Paper', 2 : 'Scissors'}
while True:
    player = int(input('Please select 0 for Rock, 1 for Paper, 2 for Scissors: '))
    computer = random.choice([0, 1, 2])
    print(f'You selected: {convention[player]} \nComputer selected: {convention[computer]}')
    winner = determine_winner(player, computer)
    print(winner)

    play_again = input('Do you want to play again? (Y/N) ').lower()
    if play_again != 'y':
        break