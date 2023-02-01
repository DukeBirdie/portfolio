# have the computer guess a random number input by the user
# generate random numbers between 0 and 100 above the user's input number
import random as r

r.seed(a=None, version=2)

uI = int(input("Input a number for the computer to guess: ",))
newNum = uI + 100
iterations = 0
while True:
    guess = r.randint(0, newNum)
    iterations += 1
    print(guess)
    if guess == uI:
        print("The computer guessed correctly.")
        break

print("Total Iterations: ", iterations)