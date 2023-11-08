from random import *

#maxNumber is highest number computer will guess
maxNumber = 100

#Waiting for user imput and calculating computer guess
print(f'I am thinking of a number from 0 to {maxNumber}')
userInput = int(input("Try to guess my number!"))
computerGuess = int(random()*maxNumber)
#this makes it repeat until user guesses correctly
while userInput != computerGuess:

  if userInput < computerGuess:
    print("Too low! Reach for the stars, dear friend!")
    userInput = int(input("Try to guess my number!"))

  if userInput > computerGuess:
    print("Too high!")
    userInput = int(input("Try to guess my number!"))

print("Correct!")