import random 
from google.colab import output

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
               

def deal_card():
    # 11 == Ace
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    new_card = random.choice(cards)
    return new_card

def calculated_score(cards):
    score = sum(cards)
    if len(cards) == 2 and score == 21:
        score = 0
    if 11 in cards and score > 21:
        for id, value in enumerate(cards):
            if value == 11:
                cards[id] = 1
                score = sum(cards)
    return score    

def compare(score_user, score_pc):
    if score_user == score_pc:
        return "The scores are the same, we have a draw."
    elif score_pc == 0:
        return "The Computer win whit a BlackJack"
    elif score_user == 0:
        return "You win whit a BlackJack"
    elif score_user > 21:
        return "The Computer win."
    elif score_pc > 21:
         return "You win."
    elif score_user > score_pc:
        return "You win."
    elif score_pc > score_user:
        return "The Computer win."

def play_game():
    quest = 'y'
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    computer_score = calculated_score(computer_cards)
    user_score = calculated_score(user_cards)
    print(logo)

    print(f"Your Cards: {user_cards} User Score: {user_score}")
    print(f"First Computer Card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        quest = 'n' 
    while quest == 'y' and score < 22:
        quest = input("Do you want to draw another card? Y or N: ").lower()
        print(f"User Cards: {user_cards} User Score: {user_score}")
        if quest != 'y':
            while computer_score != 0 and computer_score < 17:
                computer_cards.append(deal_card())
                computer_score = calculated_score(computer_cards)
        else:
            user_cards.append(deal_card())
            user_score = calculated_score(user_cards)
            output.clear()
            print(logo)
            print(f"User Cards: {user_cards} User Score: {user_score}")
    
    output.clear()
    print(logo)
    print(f"Your Final hand: {user_cards} Final Score: {user_score}")
    print(f"Computer Final hand: {computer_cards} Computer FinalScore: {computer_score}")
    print(compare(user_score,computer_score))

    while input("Do you want to play again?: Y or N: ").lower() == "y":
        output.clear()
        play_game()
        
play_game() 

print("\n************************************************")
print("************ THANK YOU FOR Play THE ************")
print("************       BLACKJACK :)     ************")
print("************************************************\n\n")
