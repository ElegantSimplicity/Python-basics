import random

def get_player_choice():
    while True:
        player_choice = input('Please select: ')
        try:
            player_choice = int(player_choice)
            if player_choice in [0, 1, 2]:
                return player_choice
        except ValueError:
            pass
        print('Invalid input. Please enter 0, 1, or 2.')

def determine_winner(player, computer):
    winner = (3 + player - computer) % 3

    match winner:
        case 0: return 'TIE'
        case 1: return 'Player WON'
        case 2: return 'Computer WON'

def update_score(player, computer):
    winner = (3 + player - computer) % 3
    global player_score
    global computer_score

    match winner:
        case 0: player_score += 1; computer_score += 1
        case 1: player_score += 2
        case 2: computer_score += 2

def play_again():
    play_again = input('Do you want to play again? (Y/N) ').lower()
    return play_again == 'y'

convention={0 : 'Rock', 1 : 'Paper', 2 : 'Scissors'}
player_score = 0
computer_score = 0

print('Welcome to Rock, Paper, Scissors!'.upper())
print('How to play: select 0 for Rock, 1 for Paper, 2 for Scissors')
while True:
    player = get_player_choice()
    computer = random.choice([0, 1, 2])
    print(f'You selected: {convention[player]}')
    print(f'Computer selected: {convention[computer]}')
    winner = determine_winner(player, computer)
    print(f'Result: {winner}')
    update_score(player, computer)
    print(f'Score: Player vs Computer {player_score} - {computer_score}\n')

    if not play_again():
        break

print('THANK YOU FOR PLAYING !')
