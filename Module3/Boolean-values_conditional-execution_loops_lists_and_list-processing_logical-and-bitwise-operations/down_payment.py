"""
Compute the down payment based on credit status.
- 10% of price if good_credit is True
- 20% of price otherwise
"""
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2*price
print(f"Down payment: {down_payment}")