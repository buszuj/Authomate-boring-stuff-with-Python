# this is a 'Guess the number game'
import random

print('Hello, What is your name?')
name = input()

print("Well, " + name + ", I am thinking about number between 0-20! Can you guess it?" )
secretNumber = random.randint(0, 20)

print('!!! DEBUG: the secret Nb is: ' + str(secretNumber) + "!!!")


#loop that will as the player, up to six times to guess the number
for tries in range(1, 7):
    print('Take a guess!')
    guess = int(input()) #since playe inputs str, we are turning it into int to use it later...

    try: 
        if guess  < secretNumber:
            print('Your guess is too low! try again')
        elif guess > secretNumber:
                print('Your guess is too hight, give it another go!')
        
        else:
            break # stop the loop when the number is guessed!
    except ValueError:
        print('You must enter a number')
        
if guess == secretNumber:
    print('You guessed the number!! You did it in '+ str(tries) + ' guesses!')
else:
    print("Nope, you took "+ str(tries) + ' guesses and missed it! My secret number was ' + str(secretNumber) + '!!')
    

