FAHRENHEIT_TO_CELCIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit): 
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius of Fahrenheit? (C/F): ").strip().upper()
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            print("Invalid unit entered. Enter celsius of fahrenheit.")
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
if __name__ == "__main__":
    main()
