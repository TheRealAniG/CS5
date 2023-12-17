# coding: utf-8
#
# hw0pr2rps.py
#

import random          # imports the library named random

def rps():
    """This plays a game of rock-paper-scissors
       (or a variant of that game)
       Arguments: none     (prompted text doesn't count as an argument)
       Results: none       (printing doesn't count as a result)
    """
    user = input("Choose your weapon(rock,paper,scissors): ")
    comp = random.choice(['rock', 'paper', 'scissors'])
    print()

    print('The user (you)   chose', user)
    print('The computer (I) chose', comp)
    print()

    if user == 'rock' and comp == 'scissors':
        print('Your rock crushes my scissors, you win :(')

    elif user == 'paper' and comp == 'rock':
        print('Your paper covers my rock, you win :(')

    elif user == 'scissors' and comp == 'paper':
        print('Your scissors cut my paper, you win :(')

    elif user == 'rock' and comp == 'paper':
        print('My paper covers your rock!, I win!')
        print("Better luck next time...")
    
    elif user == 'paper' and comp == 'scissors':
        print('My scissors cut your paper! I win!!')
        print("Better luck next time...")

    elif user == 'scissors' and comp == 'rock':
        print('My rock crushes your scissors!, I win!')
        print("Better luck next time...")

    elif (user == 'scissors' and comp == 'scissors') or (user == 'rock' and comp == 'rock') or (user == 'paper' and comp == 'paper'):
        print('We picked the same weapon and tied, Good Game')

