from google.colab import output
import random 

def chose_difficulty():
    c_difficulty = ''
    while c_difficulty != 'easy' or  c_difficulty != 'hard':
        c_difficulty = input("Chose a difficulty. Type 'easy' or 'hard': ").lower()
        if c_difficulty == 'easy':
            return 10 
        elif c_difficulty == 'hard':
            return 5
        

def chose_number():
    return random.randint(1,101)

def make_a_guess(total_attempts, chose_num):
    guess = int(input("Make a guess: "))
    if guess > chose_num:
        print("Too High")
        total_attempts -= 1
    elif guess < chose_num:
        print("Too Low")
        total_attempts -= 1
    else:
        print("Woou!! You hit the nail on the head!")
        return 0 

    if total_attempts == 0:
       print("You Lose")
       return 0
    else:
        return total_attempts

    
def game():

    logo = """
           ╔╦╗┬ ┬┌─┐  ╔╗╔┬ ┬┌┬┐┌┐ ┌─┐┬─┐     
            ║ ├─┤├┤   ║║║│ ││││├┴┐├┤ ├┬┘     
            ╩ ┴ ┴└─┘  ╝╚╝└─┘┴ ┴└─┘└─┘┴└─     
        ╔═╗┬ ┬┌─┐┌─┐┌─┐┬┌┐┌┌─┐  ╔═╗┌─┐┌┬┐┌─┐
        ║ ╦│ │├┤ └─┐└─┐│││││ ┬  ║ ╦├─┤│││├┤ 
        ╚═╝└─┘└─┘└─┘└─┘┴┘└┘└─┘  ╚═╝┴ ┴┴ ┴└─┘
"""

    output.clear()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty = chose_difficulty()
    number = chose_number()
    while range(difficulty):
        print(f"You have {difficulty} attempts remaining to guess the number.")
        difficulty = make_a_guess(difficulty, number)
    
    game = input("Do you want to play again? Yes or No: ").lower()
    if game != 'yes':
        output.clear()
        print(logo)
        print("\n************************************************")
        print("************ THANK YOU FOR PLAY THE ************")
        print("************ Number Guessing Game:) ************")
        print("************************************************\n\n")
        return True
    else:
        return False 

game_over = False 
while not game_over:
   game_over = game()
