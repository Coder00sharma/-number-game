n=40
number_of_guesses=1
print("number of guesses is only valid for 10 times")
while number_of_guesses<=10:
    guess = int(input("Enter your choice"))
    if guess >40:
        print("You guessed a greater number")
    elif guess<40:
        print("You guessed the lowest number")
    else:
        print("Congrats..! you won..")
        print(number_of_guesses,"number of guess you took to finish the game")
        break
    print(10-number_of_guesses,"guesses left")
    number_of_guesses = number_of_guesses+1
if (number_of_guesses>10):
    print("game over")






