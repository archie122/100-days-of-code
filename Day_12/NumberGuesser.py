from art import logo
import random

GUESSING_NUMBER = random.randint(1, 100)
lives = 0

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
user_choice = input("Choose a difficulty. Type 'easy' or 'hard' : ")

if user_choice == "easy":
  lives = 10
else :
  lives = 5

print(f"You have {lives} attempts remaining to guess the number.")

while lives != 0:
  user_guess = int(input("Make a guess : "))
  if user_guess > GUESSING_NUMBER:
    if lives == 1:
      print("You've run out of guesses, you lose.")
      lives = 0
    else:
      print("Too high\nGuess again")
      lives -= 1
  elif user_guess == GUESSING_NUMBER:
    print(f"You got it! The answer was {GUESSING_NUMBER}.")
    lives = 0
  else :
    if lives == 1:
      print("You've run out of guesses, you lose.")
      lives = 0
    else :
      print("Too low\nGuess again")
      lives -= 1