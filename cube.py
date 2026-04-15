# 1) Start the program.
# 2) Define a function named 'cube' that takes one input 'number'.
# 3) Inside 'cube':
# - Multiply the number by itself three times.
# - Return the result.
# 4) Define another function named 'by_three' that takes one input 'number'.
# 5) Inside 'by_three':
# - Check if the number is divisible by 3 using modulus (%).
# 6) If divisible by 3:
# - Call the 'cube' function with that number.
# - Return the result.
# 7) Else:
# - Return False.
# 8) Call the function 'by_three' with a number (like 9).
# 9) Print the result.
# 10) Call the function again with another number (like 4).
# 11) Print the result.
# 12) End the program.

def number(number):
   number2=number * number * number
   return (number2)

def by_three(number3):
    if number3 %3 == 0:
        return number(number3)
    else:
        return False
print(by_three(12))