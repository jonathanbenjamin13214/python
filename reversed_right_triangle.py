print("reversed right triangle pattern of stars")
amount = int(input("how many rows of stars do you want: "))
for i in range(0, amount):
    for j in range(0, amount - i - 1):
        print(" ", end="")
    for j in range(0, i + 1):
        print("*", end="")
    print()