import random
import os


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def cal_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def comapre(user_score, cpu_score):
    if user_score > 21 and cpu_score > 21:
        return "You went over. You lose 😤"
    if user_score == cpu_score:
        return "Draw 🙃"
    elif cpu_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif cpu_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > cpu_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    user_cards = []
    cpu_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        cpu_cards.append(deal_cards())

    while not game_over:
        user_score = cal_score(user_cards)
        cpu_score = cal_score(cpu_cards)
        print(f" your cards: {user_cards}, current score: {user_score}")
        print(f" cpu first card: {cpu_cards[0]}")

        if user_score == 0 or cpu_score == 0 or user_score > 21:
            game_over = True
        else:
            user_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_deal == "y":
                user_cards.append(deal_cards())
            else:
                game_over = True

    while cpu_score != 0 and cpu_score < 17:
        cpu_cards.append(deal_cards())
        cpu_score = cal_score(cpu_cards)
    print(f" Your final hand: {user_cards}, final score: {user_score}")
    print(f" cpu's final hand: {cpu_cards}, final score: {cpu_score}")
    print(comapre(user_score, cpu_score))


while input(
        "do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    os.system('cls' if os.name == 'nt' else 'clear')
    play_game()
