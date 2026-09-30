print("You need to guess the number from 1 to 50 with only 5 chances!")
i = 1
l = 5
while i <= 5:
    guess_num = int(input("Guess the number: "))
    sec_num = 15
    if guess_num == sec_num:
        print("Congratulations! You have guessed the number correctly!")
        break
    elif guess_num <= 14 and guess_num >= 12 or guess_num >= 15 and guess_num <= 17 :
        print("Very close.")
    elif guess_num <= 11 and guess_num >= 9 or guess_num >= 18 and guess_num <= 21 :
        print("Close.")
    elif guess_num <= 8 and guess_num >= 1 or guess_num >= 22 and guess_num <= 50:
        print("Far.")
    else:
        print("It is an invalid number.")
    i = i + 1
    l = l- 1
    print("Chances remaining: ",l)
