try:
    number = int(input("enter a number: "))
    print("the number you enterd is")
except ValueError as ex:
    print("exeption", ex)