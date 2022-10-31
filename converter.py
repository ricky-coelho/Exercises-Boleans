def temp(celsisus): 
    msg_1 = " degrees Celsius are "
    msg_2 = " degrees Farhenheit. "
    result = (celsisus * 9/5) + 32
    return str(celsisus) + msg_1 + str(result) + msg_2

user_input = input ("Enter a temperature in degrees Celsius: ")
farhennheit_result = temp(float(user_input))

if float(user_input) > 38:
    print("It's really hot!")

print(farhennheit_result)
