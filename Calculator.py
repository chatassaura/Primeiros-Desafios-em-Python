from google.colab import output

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

calc_runing = True 

def add(f_num, n_num):
  return f_num + n_num
def subtract(f_num, n_num):
  return f_num - n_num
def multiply(f_num, n_num):
  return f_num * n_num
def divide(f_num, n_num):
  return f_num / n_num

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

while calc_runing:
  output.clear()
  print(logo)
  continue_operation = True  
  f_num = float(input("What's the first number?: "))
  while continue_operation:
    n_num = float(input("What's the next number?: "))
    for key in operations:
      print(key)
    op = input("Pick an operation: ")
    calculation_function = operations[op]
    answer = calculation_function(f_num, n_num)
    print(f"{f_num} {op} {n_num} = {answer}")

    quest = input(f"Do you want to continue the operation with {answer}? Yes or No:").lower()
    if quest != "yes":
      continue_operation = False
    else:
      f_num = answer
      output.clear()
      print(logo)

calculator(f_num, op, n_num)
