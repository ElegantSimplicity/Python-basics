# Rock Paper Scissor
def determine_winner(player,computer):
    win_rule = {('rock','scissors'), ('scissors','paper'), ('paper','rock')}
    if (player,computer) in win_rule:
        return "player WON"
    elif player == computer:
        return "TIE"
    else:
        return "computer WON"

def main():
    import random
    player = input('Please select Rock, Paper, or Scissors: ').lower()
    computer = random.choice(['Rock', 'Paper', 'Scissors']).lower()
    print('computer selected: ',computer)
    print('Result: ',determine_winner(player,computer))

if __name__ == "__main__":
    main()
