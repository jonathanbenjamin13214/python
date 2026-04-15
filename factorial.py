# 1) Start the program.

# 2) Define a function named 'factorial' that takes one input 'x'.

# 3) Inside the function:
#     - Add a docstring to describe what the function does.

# 4) Check the base condition:
#     - If x is 0 or 1, return 1.
#     (Because factorial of 0 and 1 is 1)

# 5) Else:
#     - Multiply x with factorial of (x - 1).
#     - This is a recursive call (function calling itself).

# 6) End the function.

# 7) Print the docstring of the function using factorial.__doc__.

# 8) Call the function with different values (0, 1, 2, 5, 10).

# 9) Print the results with proper messages.

# 10) End the program.

def factorial(x):
    """finding the factorial"""
    if x==0 or x==1:
        return 1
    else:
        x= x * factorial(x-1)
        return(x)
print(factorial(3))