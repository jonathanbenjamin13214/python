"""Three cyclists are riding at the speed of 10,20,30 km/h. find the average and compare which cyclist is riding slower than the average speed?"""
"""
if avg > a and avg > b and avg > c:
elif avg > a and avg > b:
elif avg > a and avg > c:
elif avg > b and avg > c:
elif avg > a:
elif avg > b:
elif avg > c:
else:"""
a=10
b=20
c=30
avg=((a+b+c)/3)
print(a)
if avg > a and avg > b and avg > c:
    print("%d is higher than %d, %d, %d" %(avg, a, b, c))
elif avg > a and avg > b:
    print("%d is higher than %d, %d" %(avg, a, b))
elif avg > a and avg > c:
    print("%d is higher than %d, %d" %(avg, a, c))
elif avg > b and avg > c:
    print("%d is higher than %d, %d" %(avg, b, c))
elif avg > a:
    print("%d is higher than %d" %(avg, a))
elif avg > b:
    print("%d is higher than %d" %(avg, b))
elif avg > c:
    print("%d is higher than %d" %(avg, c))
else:
    print("invalid input")