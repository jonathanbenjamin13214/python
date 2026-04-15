# 1) Start the program.
# 2) Define a function named 'total_calc' that takes two inputs:
# - bill_amount
# - tip_perc
# 3) Inside the function:
# - Calculate total amount by adding tip to bill.
# - Tip = bill_amount * (tip_perc / 100)
# 4) Add this tip to the original bill amount.
# 5) Store the result in a variable called 'total'.
# 6) Round the total to 2 decimal places using round().
# 7) Print the final amount in a proper sentence format.
# 8) End the function.
# 9) Call the function and pass values:
# - bill amount = 150
# - tip percentage = 20
# 10) End the program.

def total_calc(check, tip):
    total=check * (tip / 100)
    final=total + check
    a=round(final)
    print("after tip your total is", a)
x=int(input("how much was your total without tip"))
y=int(input("how much percent of your bill do you want to leave as a tip"))
total_calc(x, y)