import art
import random
import os
#Functions
def check_winner(player, computer):
    player_sum = sum(player)
    computer_sum = sum(computer)
    
    if player_sum > 21 and computer_sum > 21:
        print(art.lose)
    elif player_sum == computer_sum:
        print(art.draw)
    elif computer_sum == 0:
        print(art.lose)
    elif player_sum == 0:
        print(art.win)
    elif player_sum > 21:
        print(art.lose)
    elif computer_sum > 21:
        print(art.win)
    elif player_sum > computer_sum:
        print(art.win)
    else:
        print(art.lose)
        
    
def add_draw():
    cards = []
    stock = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    x = random.randint(0,12)
    
    return stock[x]

def check_score(player_cards):
    if len(player_cards) == 2 and sum(player_cards) == 21:
        return 0
    elif sum(player_cards) > 21 and 11 in player_cards:
        player_cards.remove(11)
        player_cards.append(1)
    
    return sum(player_cards)


def blackjack():    
    print(art.logo)  
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        player_cards.append(add_draw())
        computer_cards.append(add_draw())
    
    while not is_game_over:
        user_score = check_score(player_cards)
        computer_score = check_score(computer_cards)
        print(f"Your cards: {player_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            risk = input("Type 'y' to get another card, type 'n' to pass\n")
            if risk == "y":
                player_cards.append(add_draw())
            else:
                is_game_over = True
            
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(add_draw())
        computer_score = check_score(computer_cards)

    print(f"Your final hand: {player_cards}, Final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, Final score: {computer_score}")
    check_winner(player_cards, computer_cards)  
    
    
        
        
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system('cls||clear')
  blackjack()
  