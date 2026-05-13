empty_list = []
print(empty_list)
numbers = [1, 2, 3, 4, 5]
print(numbers)
triples = [1, 2, 3] * 3
print(triples)
aList = [100, 200, 300, 400, 500]
aList = aList [::-1]
print(aList, "\n")
L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original list :", L)
count = 0
for i in L:
    count += i
avg = count/len(L)
print("sum = ", count)
print("average = ", avg)
L.sort
print("smallest element is", L[0])
print("largest element is:", L[-1])