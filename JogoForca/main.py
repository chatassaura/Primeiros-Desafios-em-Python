from hangman_words import word_list
import hangman_art as art
import random
from google.colab import output

want_to_play = True
chances = 7
end = False
blanks = []
guesses = []
have = False 
guess = "12"

def standard():
  output.clear()
  print(art.logo + "\n\n")
  print(art.stages[chances - 1]+"\n")
  print(' '.join(blanks)+"\n")
  print('Guesses: ' + ' - '.join(guesses))

while want_to_play == True: 
  chose = random.choice(word_list)
  word_lenght = len(chose)

  for n in range(word_lenght):
    blanks.append('_')
  
  standard()

  while end == False:

    guess = (input("Guess a Letter: ")).lower()
    guesses += guess

    for position in range(word_lenght):
      if guess == chose[position]:
        blanks[position] = guess
        have = True 
        
    if have == False:
      chances -= 1

    have = False
    
    standard()

    if chances == 1 :
      end = True
      print(f"\nYou Lose - The word was: {chose}\n\n")
    elif ('_' not in blanks):
      print("\n\nYou Win\n")
      end = True
    
  play = (input("Do you want to play again? Y or N: ")).lower()
  
  if play != "y":
    want_to_play = False
    output.clear()
    print(art.logo)
    print("\n***********************************************")
    print("************ THANK YOU FOR PLAY! :) ***********")
    print("***********************************************\n\n")
  else:
    blanks = []
    chose = ''
    guesses = []
    chances = 7 
    end = False
    output.clear()
