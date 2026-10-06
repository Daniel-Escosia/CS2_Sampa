input_num1 = float(input("Input the first number: "))
input_num2 = float(input("Input the second number: "))
add_numbers = input_num1 + input_num2
subtract_numbers = input_num1 - input_num2
multiply_numbers = input_num1 * input_num2
input_operation = input("1 for addition, 2 for subtraction, 3 for multiplying, 4 for dividing: ").strip()
if input_operation == "1":
  print("The sum is:", add_numbers)
elif input_operation == "2":
  print("The difference is:", subtract_numbers)
elif input_operation == "3":
  print("The product is:", multiply_numbers)
elif input_operation == "4":
  if input_num2 == 0:
    print("Pick another number other than zero for the divisor.")
  else:
    divide_numbers = input_num1/input_num2
else:
  print("Not a valid operation.")
