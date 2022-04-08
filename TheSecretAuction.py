logo = '''
    ___________
    \         /
     )_______(
     """""""|_.-._,.---------.,_.-._
     |       | | |               | | ''-.
     |       |_| |_             _| |_..-'
     |_______| '-' `'---------'` '-'
     )"""""""(
    /_________\\
   .-------------.
  /______________\\
'''

from google.colab import output
there = True
list_bidders = []

def new_bidder(name, bid):
    bidders = {}
    bidders[name] = bid    
    list_bidders.append(bidders)

while there:
  output.clear()
  print(logo)
  print("Welcome to the secret auction program.")
  name = input("What is your name?: ")
  bid = int(input("What is your bid?:$ "))
  new_bidder(name, bid)

  quest = input("Are there any other bidders? Type 'yes' or 'No'")
  if quest != "yes":
    there = False
    output.clear()
    print(logo + "\nThe secret auction program")

for id,bidder in enumerate(list_bidders):    
  for item in bidder:
    if bidder[item] > bigger:
      bigger = bidder[item]
      winner = item 

print(f"The winner is {winner} with a bid of ${bigger}.")
