
import random
from art import logo

# deal_card() function that returns a random card


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def play_game():
    print(logo)
    is_game_over = False
    # Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []

    for card in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # calculate_score() takes a List of cards as input and returns the score.

    def calculate_score(current_cards):
        # If the score is already over 21, remove the 11 and replace it with a 1.
        if 11 in current_cards and sum(current_cards) > 21:
            current_cards.remove(11)
            current_cards.append(1)
            return sum(current_cards)
        if sum(current_cards) == 21:
            return 0

    computer_score = calculate_score(computer_cards)
    user_score = calculate_score(user_cards)
    print(f'Your cards: {user_cards}, current score: {user_score}')
    print(f'Computers first card: {computer_cards[0]}')

    def compare(user_score, computer_score):
        if computer_score == user_score:
            print('Draw')
        elif computer_score == 21 or user_score > 21:
            print('You Lose.')
        elif user_score == 21 or computer_score > 21 or user_score > computer_score:
            print('You Win.')
        elif computer_score > user_score:
            print('You Lose.')

    # If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

    if computer_score == 0 or user_score == 0 or user_score > 21:
        is_game_over = True

    # If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

    while is_game_over == False:
        continue_game = input(
            'Type \'y\' to get another card, type \'n\' to pass: ')
        if continue_game == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print(f'Your cards: {user_cards}, current score: {user_score}')
            if user_score == 0:
                print('You win with blackjack.')
                is_game_over = True
            elif user_score > 21:
                print('You went over.')
                is_game_over = True
        elif continue_game == 'n':
            while computer_score < 17:
                computer_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)
            print(f'Your final hand: {user_cards}, final score: {user_score}')
            print(
                f'Computer\'s final hand: {computer_cards}, final score: {computer_score}')
            is_game_over = True

    # Compares the user score with the computer score and determines whether it is a win, a lose, or a draw.

    compare(user_score, computer_score)


# Asks user whether the want to continue playing or stop.
while input('Do you want to play a game of Blackjack? Type \'y\' or \'n\'. ') == 'y':
    play_game()
