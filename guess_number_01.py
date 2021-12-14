import random

def guess(x):
    random_number = random.randint(0, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x} '))
        if guess < random_number:
            print('Sorry,guess again.Too low')
        elif guess > random_number:
            print ('Sorry,guess again. Too high')
    
    print('You have guessed the number')


guess(20)










