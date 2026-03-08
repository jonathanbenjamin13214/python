
"""Write a program to calculate the electricity bill. The bill is calculated by checking the number of units consumed. Suppose the user is consuming less than 50 units. The per-unit cost will be 2.60, and the tax on that bill will be 25. If a user is consuming more than 50 but less than 100. Then the per-unit cost will be 3.25, and the tax on that bill will be 35 If the user is coming more than 100 and less than 200. Then the per-unit cost will be 5.26, and the tax will be 45 And above 200, the cost of the unit is 8.45, and the tax is 75."""
a=int(input("how many megabites of electricity did you use"))
if(a<50):
    a1=a*2.60+25
    print(a1)
elif(a<=100):
    a2 = 130 + ((a- 50) * 3.25)+35
    print(a2)
elif(a<=200):
    a3 = 130 + 162.50 + ((a - 100) * 5.26)+45
    print(a3)
else:
    print(130 + 162.50 + 526 + ((a- 200) * 8.45)+75)