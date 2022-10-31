weather = "sunny"
temperature = "cold"

if weather == "raining" and temperature == "cold":
    print("Take an umbrella and a warm jacket")
elif weather == "raining" and temperature == "warm": # with And both checks must be ==
    print("Take an umbrella and a t-shirt")
elif weather == "sunny" and temperature == "cold":
    print("Take sunglasses and a warm jacket")
elif weather == "sunny" and temperature == "warm":
    print("Take an umbrella and a t-shirt")
else:
    print("Stay home")