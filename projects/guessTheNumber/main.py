# guess the number that the computer generates
import random as r

# sets the random seed
r.seed(a=None, version=2)
rand = r.randint(0, 10) # sets the random number

while True:
    guess = int(input("Input a guess: ")) # the user guesses
    if guess == rand:
        print("You guessed correctly!")
        False