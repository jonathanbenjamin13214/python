num = input("Enter a number: ")

clean_num = num.replace("-", "")

digit_count = 0
i = 0

while i < len(clean_num):
    digit_count += 1
    i += 1

print("Total digits:", digit_count)