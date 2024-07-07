FAHRENHEIT_TO_CELCIUS_FACTOR = 5 /9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit): 
    return (fahrenheit - 32 ) * FAHRENHEIT_TO_CELCIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) +32


def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius of Fahrenheit (C/F): ").strip().upper()
    if unit == "C":
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted_temp}°F")
    elif unit == "F":
        converted_temp = convert_to_celsius(temp)
        print(f"{temp}°F is {converted_temp}°C")
    else:
        print(f"Invalid input. Please specify 'C' for Celsius or 'F' for fahrenheit.")
        return
    
if __name__ == "__main__":
    main()