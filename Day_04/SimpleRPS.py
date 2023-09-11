import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print("Hello, and welcome to a simple rock paper scissors game!!")

rps_list = [rock, paper, scissors]

user_choice = rps_list[int(input("What do you choose? Tyoe 0 for Rock, 1 for Paper and 2 for Scissors : "))]
comp_choice = rps_list[random.randint(0,2)]

print("\nYour choice : ")
print(user_choice)
print("Computer choice : ")
print(comp_choice)

if user_choice == comp_choice :
  print("Draw")
elif (user_choice == rock and comp_choice == scissors) or (user_choice == scissors and comp_choice == paper) or (user_choice == paper and comp_choice == rock):
  print("You Win!!")
else :
  print("You Lose")
