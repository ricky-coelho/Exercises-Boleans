def play():
    secret_number = 8
    secret_color = "red"

    guess_number = input("Enter a number between 1 and 20: ") # this needs to bo converted to an integer
    guess_color = input("Enter a color: ")

    if secret_number == int(guess_number) and secret_color == guess_color:
        print("Congratulations! You figured out both secrets!")
    elif secret_number == int(guess_number) or secret_color == guess_color: # only 1 is found
        print("Great! you foun one of the secrets!")
    else:
        print("You didn't find any of the secrets...")
        print("Better luck next time!")

    print("Try again") # executed regardless of the result before

play()