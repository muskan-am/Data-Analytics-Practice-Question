#  Write a program to convert temperature from
#     Celsius to Fahrenheit by creating a function.

def convert(c):
    return (c * 9/5) + 32


celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = convert(celsius)

print("Temperature in Fahrenheit:", fahrenheit)
