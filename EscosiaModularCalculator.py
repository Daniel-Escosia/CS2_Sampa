num1 = float(input("Input the first number: "))
num2 = float(input("Input the second number: "))
def add_numbers(a, b):
  return a + b
def subtract_numbers(a, b):
  return a - b
def multiply_numbers(a, b):
  return a * b
def divide_numbers(a, b):
  if b == 0:
    return "Cannot divide by zero."
  else:
    return a / b
operation = int(input("1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: ").strip())
if operation == 1:
  result = add_numbers(num1, num2)
  print(result)
elif operation == 2:
  result = subtract_numbers(num1, num2)
  print(result)
elif operation == 3:
  result = multiply_numbers(num1, num2)
  print(result)
elif operation == 4:
  result = divide_numbers(num1, num2)
  print(result)
else:
  result = "No valid operation."
  print(result)
