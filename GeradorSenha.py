#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

senha = []
for n in range (0,(nr_letters)):
  #password += random.choice(letters) // modo da professora 
  r_letter = int(random.randint(0,len(letters)-1))
  senha.append(letters[r_letter])

for n in range (0,(nr_numbers)):
  #password += random.choice(numbers) // modo da professora 
  r_numbers = int(random.randint(0,len(numbers)-1))
  senha.append(numbers[r_numbers])

for n in range (0,(nr_symbols)):
  #password += random.choice(symbols) // modo da professora 
  r_symbols = int(random.randint(0,len(symbols)-1))
  senha.append(symbols[r_symbols])

random.shuffle(senha) # comentando esta linha fica no modo fácil
senha = ''.join(senha)


print(f"You new password is: {senha}")
