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

num1 = int(input("What's the first number?: "))


for symbol in operations:
  print(symbol)

operation_symbol = input("Pick an operation from the line above: ")

num2 = int(input("What's the second number?: "))
func = operations[operation_symbol]
answer = func(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")