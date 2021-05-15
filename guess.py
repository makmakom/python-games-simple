# Game for guess integers
import random

guessesCount = 0
print('Hi, What is your name?')

userName = input()
fromNumber = 1
toNumber = 20
number = random.randint(fromNumber, toNumber)

print(
    'So, ', userName, ', I conceived a number from ', str(fromNumber),
    ' to ', str(toNumber), ', and you should guess ;P', sep=''
      )

guess = int()
for guessesCount in range(6):
    print('Try guess')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your number is to little.')

    if guess > number:
        print('Your number is to big.')

    if guess == number:
        break

if guess == number:
    print('Excellent, ', userName, '! You\'r done by ', str(guessesCount + 1), ' tries!', sep='')

if guess != number:
    print('Sorry, I conceived the number ', str(number), '.', sep='')
