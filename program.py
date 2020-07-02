# Very basic rock paper scissors game using python.
# Made by @abhiyanbeta.
#
# Instructions: run the script and enter "R" for rock, "P" for paper or "S" for scissors.
# The computer will randomly select a choice and determine the winner. The winner is awarded
# one point and the scoreboard is displayed. The game then restarts.
#
# Limitations:
#     - The ability to set one game as being a number of rounds.
#     - The ability to play two-player instead of against the computer.
#     - The ability to reset the game.
#

import random

# Display header
print("----------------------------")
print("    ROCK PAPER SCISSORS     ")
print("----------------------------")

# Display game instructions
print("Welcome to rock paper scissors game. "
      "You will be asked to pick an option (rock, paper or scissors).\n"
      "The computer will then randomly pick it's choice."
      "The winner will be awarded 1 point and the round will restart.")

# Obtain an input from the user (rock, paper or scissors)
user_input = ''  # global user_input variable
computer_input = ''  # global computer_input variable


def obtain_user_input():
      global user_input
      user_input = input("Enter [R]ock, [P]aper or [S]cissors: ").lower()
      if user_input == "r":
            user_input = "rock"
      elif user_input == "p":
            user_input = "paper"
      elif user_input == "s":
            user_input = "scissors"
      else:
            print("Invalid input.")
      print("You have selected {}.".format(user_input))


# Obtain a random input from the computer
def obtain_computer_input():
      global computer_input
      list = ["rock", "paper", "scissors"]
      computer_input = random.choice(list)
      print("The computer has selected {}.".format(computer_input))


# Calculate who wins
user_score = 0  # global user_score variable
computer_score = 0  # global computer_score variable


def compute_who_wins():
      global user_input, computer_input, user_score, computer_score
      if user_input == computer_input:
            print("Draw. You both get 1 point each.")
            user_score += 1
            computer_score +=1
      elif user_input == "rock" and computer_input == "scissors":
            print("User wins")
            user_score += 1
      elif user_input == "rock" and computer_input == "paper":
            print("Computer wins")
            computer_score +=1
      elif user_input == "paper" and computer_input == "rock":
            print("User wins")
            user_score += 1
      elif user_input == "paper" and computer_input == "scissors":
            print("Computer wins")
            computer_score +=1
      elif user_input == "scissors" and computer_input == "rock":
            print("Computer wins")
            computer_score +=1
      elif user_input == "scissors" and computer_input == "paper":
            print("User wins")
            user_score += 1
      else:
            print("Unable to determine winner.")


# Update scoreboard and display
def print_result():
      global user_score, computer_score
      print("Score: User {} Computer {}".format(user_score, computer_score))


# STARTS & LOOPS OVER GAME
start_input = input("To start the game press [S]tart or [E]xit: ").lower()
if start_input == "s":
      start_input = True
      while start_input:
            obtain_user_input()
            obtain_computer_input()
            compute_who_wins()
            print_result()
      else:
            pass
elif start_input == "e":
      print("Bye!")
      exit()
else:
      print("Invalid input.")

