import random, sys
again = True

while True:
    while True:
        print("Please select (R)ock, (P)aper, or (S)cissors or (Q)uit")
        userChoice = str(input())
        if userChoice == 'Q':
            sys.exit()
        elif userChoice == 'R' or userChoice == 'P' or userChoice == 'S':
            break

    opponent = random.randrange(1,4)
    if opponent == 1:
        opponent = 'R'
    elif opponent == 2:
        opponent = 'P'
    elif opponent == 3:
        opponent = 'S'
    
    if userChoice == 'R' and opponent == 'R':
        print('Rock vs Rock! Tie!')
    elif userChoice == 'R' and opponent == 'P':
        print('Rock vs Paper! You lose!')   
    elif userChoice == 'R' and opponent == 'S':
        print('Rock vs Scissors! You win!')   
    elif userChoice == 'P' and opponent == 'P':
        print('Paper vs Paper! Tie!')
    elif userChoice == 'P' and opponent == 'R':
        print('Paper vs Rock! You win!') 
    elif userChoice == 'P' and opponent == 'S':
        print('Paper vs Scissors! You lose!')  
    elif userChoice == 'S' and opponent == 'P':
        print('Scissors vs Paper! You win!')
    elif userChoice == 'S' and opponent == 'R':
        print('Scissors vs Rock! You lose!')  
    elif userChoice == 'S' and opponent == 'S':
        print('Scissors vs Scissors! Tie!')
