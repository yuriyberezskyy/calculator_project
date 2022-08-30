import art

print(art.logo)
#Add
def add(n1,n2):
  return n1+n2

#Subtract
def subtract(n1,n2):
  return n1-n2

#Multiply
def multiply(n1,n2):
  return n1*n2

#Devide
def devide(n1,n2):
  return n1/n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": devide
}


def calculation():
  num1 = int(input("What's the first number?: "))
  
  is_next_number = True  
  
  while(is_next_number):
    for symbol in operations:
      print(symbol)
    
    operation_symbol = input("Pick an operation from the line above: ")
    
    num2 = int(input("What's the next number?: "))
    func = operations[operation_symbol]
    answer = func(num1,num2)
  
    is_next_step = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
  
    if is_next_step == 'y':
      num1 = answer
    else:
      is_next_number = False
      calculation()

calculation()