player = input("Rock Paper Scissor? ")
from random import randint
computer = randint(1,3)
match computer:
    case 1: print('Computer select: Rock')
    case 2: print('Computer select: Paper')
    case 3: print('Computer select: Scissor')
match player:
    case 'Rock':
        match computer:
            case 1: print('Draw')
            case 2: print('Lose')
            case 3: print('Win')
    case 'Paper':
        match computer:
            case 1: print('Win')
            case 2: print('Draw')
            case 3: print('Lose')
    case 'Scissor':
        match computer:
            case 1: print('Lose')
            case 2: print('Win')
            case 3: print('Draw')
  
