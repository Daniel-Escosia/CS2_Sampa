num1 = float(input("Input the first number: "))
num2 = float(input("Input the second number: "))
def add_numbers():
  sum = num1+num2
  print("The sum is:", sum)
def subtract_numbers():
  difference = num1-num2
  print("The difference is:", difference)
def multiply_numbers():
  product = num1*num2
  print("The product is:", product)
def divide_numbers():
  if num2 == 0:
    print("Cannot divide by 0.")
  else:
    quotient = num1/num2
    print("The quotient is:", quotient)
operation = int(input("1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: ").strip())
if operation == 1:
  add_numbers()
elif operation == 2:
  subtract_numbers()
elif operation == 3:
  multiply_numbers()
elif operation == 4:
  divide_numbers()
else:
  print("No valid operation.")
