import random

low = 1
high = 20
print('Hello, What is you name?')
name = input()
print('Hi, My name is ' + name)
print('Take a guess')
secretNumber = random.randint(low, high)
print('Well, ' + name + ' I am thinking of a number between ' + str(low) + ' and ' + str(high))

for guessesTaken in range(0, 7):
    print('Take a guess: ')
    guess = int(input())
    if guess < secretNumber:
        print('A bit higher')
    elif guess > secretNumber:
        print('A bit lower')
    else:
        break

if guess == secretNumber:
    print('Yea ' + name + ' your guess is correct')
else:
    print('Nope,' + name + ' you are wrong')