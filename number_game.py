import random
playing = True
number = str(random.randint(0, 9))
print("I'm choosing a number between 1 and 9 and you need to guess it")
while playing:
    guess = input("choose a number and type it in \n")
    if number == guess:
        print("you guessed correctly! good job")
        break
    else:
        print("Nope! guess again \n")