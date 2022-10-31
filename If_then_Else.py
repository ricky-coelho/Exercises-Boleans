secret_number = 7
guess = input("Enter a number between 1 and 10: ")

if secret_number == int(guess):
    print("You win!")
else:
    print("You lose!")

print("Try to play again!")