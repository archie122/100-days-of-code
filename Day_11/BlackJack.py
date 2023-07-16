import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
comp_cards = []


def deal_card(card, number_of_cards=1):
  if number_of_cards == 1:
    card.append(random.choice(cards))
    if sum(card) > 21 and 11 in card:
      for i in range(0, len(card)):
        if card[i] == 11:
          card[i] = 1
  else:
    card.append(random.choice(cards))
    card.append(random.choice(cards))


def end_program():
  print("Thanks you for playing!!!!")


def show_hands():
  print(f"\tYour cards: {user_cards}, current score: {sum(user_cards)}")
  print(f"\tComputer's first card: {comp_cards[0]}")


def show_final_hands():
  print(f"\tYour final hand: {user_cards}, final score: {sum(user_cards)}")
  print(
    f"\tComputer's final hand: {comp_cards}, final score: {sum(comp_cards)}")


def check_win():
  if sum(user_cards) >= 21 or sum(comp_cards) >= 21:
    return True
  return False


def check_hands():
  while sum(user_cards) < 21 and sum(comp_cards) < 21:
    if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
      #something
      deal_card(user_cards)
      deal_card(comp_cards)

      if check_win():
        show_final_hands()
      else:
        show_hands()
    else:
      #something
      deal_card(comp_cards)

      if check_win():
        show_final_hands()
      else:
        show_hands()

  if sum(user_cards) > 21:
    return "You went over. You lose"
  elif sum(comp_cards) > 21:
    return "Opponent went over. You won"
  elif sum(comp_cards) > sum(user_cards):
    return "You lost"
  elif sum(user_cards) > sum(comp_cards):
    return "You won"


def blackjack():
  user_choice = input(
    "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  clear()
  print(logo)

  if user_choice == 'n':
    end_program()
  else:
    deal_card(user_cards, 2)
    deal_card(comp_cards, 2)

    if check_win():
      show_final_hands()
    else:
      show_hands()

    print(check_hands())

    user_cards.clear()
    comp_cards.clear()
    blackjack()


blackjack()
