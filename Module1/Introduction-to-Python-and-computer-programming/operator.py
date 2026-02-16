income =  float(input("Enter the annual income: "));

if income < 85528:
    tax = income * 0.18 - 556.02  # the * has the higher priority
tax = round(tax, 0) # Rounds to the nearest whole number
print("The tax is:", tax, "thalers")

    