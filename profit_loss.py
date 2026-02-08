a = float(input("what was the buying price"))
b = float(input("what was the selling price"))
if a<b:
    c = b - a
    print(c)
    print("profit")
else: 
    d = a - b
    print(d)
    print("loss")