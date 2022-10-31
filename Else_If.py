a = input("Enter a number : ")
b = input("Enter another number :")
result = float(a) - float(b)

if result > 10:
    print("The result is greater than 10")
elif result > 0:
    print("The result is greater than 0")
elif result == 0:
    print("Result is zero")
else:
    print("Negative number !")

print("You can try again")