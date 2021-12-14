# Two guessing games: 
# 01. The computes computes a number that you have to guess
# 02. The computer has to guess your computed number
    
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


#guess(20)

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high: #the computer would be mistaken if they are equal
            guess = random.randint(1, x)
        else:
            guess = low #could also be high
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)??')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Haha, I have guessed the number {guess}. Give me a harder one!')

computer_guess(27)









