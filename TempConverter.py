# Function to convert Celsius to Fahrenheit
def convert_temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Input from user
celsius = float(input("Enter temperature in Celsius: "))

# Call function
fahrenheit = convert_temperature(celsius)

# Display result
print("Temperature in Fahrenheit: {:.2f}".format(fahrenheit))