print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('Welcome to Tresure Forest.')
chose = (input("You're" + ' at a cross road. Where do you want to go?\n Type "left" or "right"\n What do you chose: ')).lower()
if(chose == "left"):
  chose = (input('You come to a Vampire Castle. There is an room with a huge shadow. \n Type "continue" to go ahead in the hall.\n Type "enter" to enter in the room\n What do you chose: ')).lower()
  if chose == 'continue':
    chose = (input('You decide to continue. then you see yourself in front of a scary vimpire.\n Type "talk" to talk to the vampire.\n Type "run" to run away from the vampire\n What do you chose: ')).lower()
    if chose == 'talk':
      print('You made a right decision, the vampire is really cool and give you a week in your castle to eat and to rest and teach you how to come back to the city.')
    else:
      print("Oooh noo, you're in trouble, the vampire is furious and sent the bats to catch you for his meal.")
  else:
    if chose == 'enter':
      chose = (input('You come to a bright room whit a realy cute dog, looking to you and a pile of gold next to him.\n Type "dog" to go to the dog and give him some affection.\n Type "gold" to go through the dog em catch the money')).lower()
      if chose == 'dog':
        print('The dog is really happy, and to show their gratitude he opem his mounth ang give you a huge and valueble diamond and a map from the region.')
      else:
        print('The dog starts to transform into a werewolf and jump on you biting you neck...')
else:
  chose = (input('You see a dense florest whit two paths. Type "left" to go to a path with a very bright light at the end of the path.\n Type "right" to go to the path with no light\n What do you chose: ')).lower()
  if chose == "left":
    chose = (input("You go ahead in the left path and found a huge spider's nest whith a girl asking for help. " + '\nType "save" to go to the girl.\n Type "back" to come back and go to the right path\n What do you chose: ')).lower()
    if chose == "save":
      print('When you get closer you realize that girl was a bait and a big spider appears and bites you in one bite.')
    else:
      right = True
  else:
    right = True
  
  if right:
    print("You go through a darkest path and realize that is the right path and see you in front of the city's park next of your house,\n and feel relieved that you come back to home and your family")


print('\n \n \n \n****** THANKS TO PLAY ********')
