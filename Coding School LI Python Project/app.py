import random

userWins = 0
compWins = 0
options = ["rock", "paper", "scissors"]

#game loop always runs until we break from it
while True:
    userInput = input("Choose Rock, Paper, or Scissors! You can also type Q to quit. ").lower()
    if userInput == 'q':
        break
    if userInput not in options:
        continue
    
    computerPick = options[random.randint(0, 2)]

    if userInput == 'rock' and computerPick == 'scissors':
        userWins += 1
        print('The computer picked ', computerPick, '. You won!')
        print(" ")

    elif userInput == 'paper' and computerPick == 'rock':
        userWins += 1
        print('The computer picked ', computerPick, '. You won!')
        print('The computer picked ', computerPick, '. You won!')


    elif userInput == 'scissors' and computerPick == 'paper':
        userWins += 1
        print('The computer picked ', computerPick, '. You won!')
        print(" ")

    elif userInput == computerPick:
        print('That one was a draw! Try again.')
        print(" ")

    else:
        compWins =+ 1
        print(f'The computer picked ', computerPick, '. Computer wins.')
        print(" ")

print("")
print('You won ', userWins, ' times.')
print('The computer won ', compWins, ' times.')
print("")

print('Bye!')
