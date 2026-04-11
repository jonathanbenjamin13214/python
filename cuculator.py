def add (P, Q):
    return P + Q
def subtract(P, Q):
    return P-Q
def multiply(P, Q):
    return P * Q
def devide(P, Q):
    return P / Q
print ("Please select the operation.")
print ("a=Add")
print ("b=Subtract")
print ("c=Multiply")
print ("d=Divide")
choise = input("choose enter your choise (a/ b/ c/ d): ")
num_1 = int (input ("please enter the first number"))
num_2 = int (input ("please enter the second number"))
if choise == "a":
    print (num_1, "+", num_2, "=", add(num_1, num_2))
elif choise == "b":
     print (num_1, "-", num_2, "=", subtract(num_1, num_2))
elif choise == "c":
     print (num_1, " * ", num_2, "=", multiply(num_1, num_2))
elif choise == "d":
     print (num_1, " / ", num_2, "=", devide(num_1, num_2))
else:
    print ("the input is invalid")