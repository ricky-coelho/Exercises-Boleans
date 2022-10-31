secret_word = "Kiwi" # une variable secrète que le user doit deviner
guess = input("What is the secret word ? ")

print(secret_word == guess) #à chaque fois que le user entre un mot, il verra false.  s'il écrit le bon mot il verra true
