from random import choice

outcomes = ['rock', 'paper', 'scisors']

player = input("rock, paper, scisors: ")

ai=choice(outcomes)

print("AI chose %s. " % ai, end='')
    
if player == ai:
    print("It's a draw")
else:
    if player == 'rock':
        if ai == 'paper':
            print("You lose")
        else:
            print("You win")

    if player == 'paper':
        if ai == 'rock':
            print("You win")
        else:
            print("You lose")

    if player == 'scisors':
        if ai == 'paper':
            print('You win')
        else:
            print('You lose')