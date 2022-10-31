var weather = "sunny"
var temperature = "warm"

if (weather == "raining" && temperature == "warm") {
    console.log("Take an umbrella and sunglasses");
} else if ( weather == "raining" && temperature == "cold") {
    console.log("Take an umbrella and a warm jacket");
} else if ( weather == "sunny" && temperature == "warm") {
    console.log("Take sunglasses and a t-shirt");
} else if ( weather == "sunny" && temperature == "cold") {
    console.log("Take sunglasses and a warm jacket");
} else {
    console.log("Stay home!")
}