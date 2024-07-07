FAHRENHEIT_TO_CELCIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(Fahrenheit): 
    global FAHRENHEIT_TO_CELCIUS_FACTOR
    return (Fahrenheit - 32 ) * FAHRENHEIT_TO_CELCIUS_FACTOR

def convert_to_fahrenheit(Celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (Celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        raise ValueError("Invalid temperature.Please enter a numeric value.")

    unit = input("Is this temperature in Celsius of Fahrenheit (C/F): ").strip().upper()
    if unit == "C":
        converted_temperature = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temperature}°F")
    elif unit == "F":
        converted_temperature = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temperature}°C")
    else:
        print("Invalid input.Please specify 'C' for Celsius or 'F' for fahrenheit.")
        
    
if __name__ == "__main__":
    main()