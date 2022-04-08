import random

print("************** GAME ***************")
print("****** Rock / Paper / Scisor ******")
print("***********************************\n")

wantToPlay = True

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


while wantToPlay:
  computer_chose = 0
  computer_chose = random.randint(0,2)
  chose = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n'))

  if chose < 0 or chose > 2:
    print("You typed an ivalid number, you lose!\n")
  else:
    if chose == 0:
      print(rock)
        
    elif chose == 1:
      print(paper)

    elif chose == 2:
      print(scissors)

      print("\n")
    
    print(f"Computer chose: {computer_chose} \n")

    if computer_chose == 0:
      print(rock)
        
    elif computer_chose == 1:
      print(paper)

    elif computer_chose == 2:
      print(scissors)

    if chose == computer_chose:
      print('A tie')
    elif chose == 0 and computer_chose == 1:
      print("You lose")
    elif chose == 0 and computer_chose == 2:
      print("You win")
    elif chose == 1 and computer_chose == 0:
      print("You win")
    elif chose == 1 and computer_chose == 2:
      print("You lose")
    elif chose == 2 and computer_chose == 0:
      print("You lose")
    elif chose == 2 and computer_chose == 1:
      print("You win")

  play = (input("Do you want to play again? Y or N: ")).lower()
  if play != 'y':
    wantToPlay = False;
    print("\n***********************************")
    print("********* Thank you to Play *******")
    print("***********************************\n")
  else:
    computer_chose = ''

  print('\n')
