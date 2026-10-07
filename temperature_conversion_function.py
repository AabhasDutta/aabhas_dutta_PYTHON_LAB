def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperature = float(input("Enter temperature in Celsius: "))

result = celsius_to_fahrenheit(temperature)

print("Temperature in Fahrenheit:", result)