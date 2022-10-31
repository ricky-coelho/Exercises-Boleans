weather = "sunny"

if weather == "sunny":
    print("It is sunny outside.")
    print("It is a beautiful day!")

print("This line of code will execute no matter what.")

#si le weather = à sunny, on aura trois messages à l'écran,
# It is sunny outside + It is a beautiful day! + This line of code will execute no matter what.
# mais si nous avons le code ci-dessous, seule la dernière sera visible car, le wather n'est pas égal à sunny

weather = "rainy"

if weather == "sunny":
    print("It is sunny outside.")
    print("It is a beautiful day!")

print("This line of code will be executed no matter what")

# greater and smaller

apple = 7
oranges = 3
if apple > oranges:
    print("There are more apples than oranges")