logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

from google.colab import output
want = True

def Caeser(direction, text, shift): 
  cipher = []
  if direction == 'encode':
    dec_aux_position = -1
    aux_position = len(alphabet)

  elif direction == 'decode':
    aux_position = 0
    dec_aux_position = len(alphabet)
    shift *= -1 

  for letter in text: 
    for position in range(len(alphabet)): 
      if alphabet[position] == letter: 
        if position == aux_position: 
          position = dec_aux_position
        if position + shift > aux_position:
          print("shift " + str(shift))
          print("position " + str(position))
          print("aux_position " + str(aux_position))
          position -= aux_position
        cipher.append(alphabet[position + shift])
    if letter not in alphabet:
      cipher.append(letter) 

  print(f"The results of the {direction} is: {''.join(cipher)}" )

def continue_encrypt(want, text, shift, direction):
  quest = (input("Do you want to use again? Y or N ")).lower()
  if quest != 'y':
    output.clear()
    want = False
    print(logo + "\n")
    print("\n***********************************************")
    print("************ THANK YOU FOR USE THE ************")
    print("************    Caeser Cipher :)   ***********")
    print("***********************************************\n\n")
    return want
  else:
    output.clear()
    want = True
    text = ''
    shift = 0 
    direction = ''
    return want
    
while want:
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  direction = ''
  print(logo + "\n")
  while direction != 'encode' and direction != 'decode' and want:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  Caeser(direction = direction, text = text, shift = shift)
  want = continue_encrypt(want, text, shift, direction)
  

