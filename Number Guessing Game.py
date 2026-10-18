print("Guess a number between 1 and 50. You have 5 chances.")

secret = 15
chances = 5

while chances > 0:
    try:
        guess = int(input("Guess the number: "))
    except ValueError:
        print("Please enter a whole number between 1 and 50.")
        continue

    if not 1 <= guess <= 50:
        print("Please enter a number between 1 and 50.")
        continue

    if guess == secret:
        print("Congratulations! You guessed the number correctly!")
        break

    diff = abs(guess - secret)
    if diff <= 1:
        print("Extremely close!")
    elif diff <= 2:
        print("Very close.")
    elif diff <= 5:
        print("Close.")
    else:
        print("Far.")

    chances -= 1
    print("Chances remaining:", chances)

else:
    print("Sorry, you're out of chances. The number was", secret)