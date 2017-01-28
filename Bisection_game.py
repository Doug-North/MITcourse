high = 100
low = 0
x = (high + low) // 2
rules = \
    "Enter 'h' to indicate the guess is too high." \
    "Enter 'l' to indicate the guess is too low." \
    "Enter 'c' to indicate I guessed correctly."

print("Please think of a number between 0 and 100! ")
print("Is your secret number {}?".format(x))
ans = str(input(rules))

while ans != 'c':
    if ans == 'h':
        high = x
        x = (x+low)//2
        print("Is your secret number {}?".format(x))
        ans = str(input(rules))
    elif ans == 'l':
        low = x
        x = (x + high)//2
        print("Is your secret number {}?".format(x))
        ans = str(input(rules))
    elif ans == 'c':
        print("Game over. Your secret number was: {}".format(x))
    else:
        print("Sorry, I did not understand your input.")
        print("Is your secret number {}?".format(x))
        ans = str(input(rules))

print("Game over. Your secret number was: {}".format(x))


