import random
from art import logo, vs
from game_data import data

# User Lives
lives = True

# Score Tracker
score = 0


# Print the Title
def print_title():
    print(logo)


# Print the VS logo
def print_VS():
    print(vs)


# Get data
def get_data():
    return random.choice(data)


print_title()
option1 = get_data()
option2 = get_data()

while lives:
    print(f"Compare A: {option1['name']}, a {option1['description']}, from {option1['country']}.")
    print_VS()
    print(f"Against B: {option2['name']}, a {option2['description']}, from {option2['country']}.")
    user_choice = input("Who has more followers? Type 'A' or 'B' : ").lower()

    if user_choice == 'a' and option1['follower_count'] > option2['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}. \n")

        option1 = option2
        option2 = get_data()
    elif user_choice == 'b' and option1['follower_count'] < option2['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}. \n")

        option1 = option2
        option2 = get_data()
    else:
        print(f"Sorry, that's wrong. Final score: {score}. \n")
        lives = False
