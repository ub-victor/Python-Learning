number1 = int(input('Enter the first number: '))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))


largest_number = number1

if number2 > largest_number:
    largest_number = number2

if number3 > largest_number:
    largest_number = number3

print("The largest number is:", largest_number);