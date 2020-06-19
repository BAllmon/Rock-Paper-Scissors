import random, sys
again = True

wins = 0
losses = 0
ties = 0

while True:
  while True:
    print("Please select (R)ock, (P)aper, or (S)cissors or (Q)uit")
    userChoice = str(input())
    if userChoice == 'Q':
        print('Thanks for playing with me!')
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
      ties += 1
  elif userChoice == 'R' and opponent == 'P':
      print('Rock vs Paper! You lose!')  
      losses += 1 
  elif userChoice == 'R' and opponent == 'S':
      print('Rock vs Scissors! You win!') 
      wins += 1   
  elif userChoice == 'P' and opponent == 'P':
      print('Paper vs Paper! Tie!')
      ties += 1
  elif userChoice == 'P' and opponent == 'R':
      print('Paper vs Rock! You win!') 
      wins += 1  
  elif userChoice == 'P' and opponent == 'S':
      print('Paper vs Scissors! You lose!') 
      losses += 1  
  elif userChoice == 'S' and opponent == 'P':
      print('Scissors vs Paper! You win!')
      wins += 1  
  elif userChoice == 'S' and opponent == 'R':
      print('Scissors vs Rock! You lose!')  
      losses += 1 
  elif userChoice == 'S' and opponent == 'S':
      print('Scissors vs Scissors! Tie!')
      ties += 1

  print('Wins: ' + str(wins) + ' Losses: ' + str(losses) + ' Ties: ' + str(ties))
