
# a) Check if the character at position `i` in `string` is equal to `char`.
# b) If yes, increase `count` by 1.
# c) Increase `i` by 1 to move to the next character.
# 6) After the loop, print how many times `char` occurred in `string` using `count`.

string=str(input("enter a word"))
char=str(input("enter a single letter"))
i=0
count=0
while i<len(string):
    if string[i]==char:
        count=count+1
    i=i+1
print(char,count)