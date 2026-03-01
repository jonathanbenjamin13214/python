character = input("Type one character: ")

# Check if the user entered exactly one character
if len(character) == 1:
    
    # Convert the character to its ASCII value
    ascii_value = ord(character)
    
    # Show the result
    print("The ASCII value of", character, "is", ascii_value)

else:
    print("Please enter only ONE character.")
