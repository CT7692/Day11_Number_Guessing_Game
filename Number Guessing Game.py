#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

###############Function Definitions:

import art as a
import secrets

def validator(option_a, option_b, prompt):
  correct = True
  user_input = input(prompt).lower()
  if (user_input != option_a) and (user_input != option_b):
    correct = False
    while not correct:
      print("\nPlease enter valid option.")
      user_input = input(prompt).lower()
      if(user_input == option_a) or (user_input == option_b):
        correct = True
  return user_input

def intro():
  print(a.logo)
  print("Welcome to Guess the Number!")
  print("\nI'm thinking of a number between 1 and 100.")

def get_difficulty(chosen_setting):
  att = 0
  if chosen_setting == "easy":
    att = 10
  elif chosen_setting == "hard":
    att = 5
  return att
  
def game(attempts):
  answer = secrets.SystemRandom().randint(1, 100)
  game_on = True
  correct_answer = False
  while game_on and attempts > 0:
    if attempts > 0 and game_on:
      status = f"\nYou have {attempts} attempts remaining to guess the number."
      print(status)
      guess = input("Guess: ")
      if not guess.isnumeric():
        print("\nNot a number. Guess again.")
      elif int(guess) > answer:
        print("\nToo high.")
        attempts -= 1
      elif int(guess) < answer:
        print("\nToo low.")
        attempts -= 1
      else:
        game_on = False
        correct_answer = True
        print(f"\nCongratulations! You got the answer: {answer}!")
    elif attempts == 0:
      game_on = False   
  if not correct_answer:
    print(f"\nThe answer was {answer}... Better luck next time!")
  return guess
    
############### Functions Defined:

diff_prompt = "Choose a difficulty. Type 'easy' or 'hard': "
intro()
difficulty = validator("easy", "hard", diff_prompt)
attempts = get_difficulty(difficulty)
player_guess = game(attempts)
