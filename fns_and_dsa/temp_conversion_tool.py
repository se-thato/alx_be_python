FAHRENHEIT_TO_CELCIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit): 
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELCIUS_FACTOR
    return round(celsius, 1)

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return round(fahrenheit, 1)


def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
         unit = input("Is this temperature in Celsius of Fahrenheit (C/F): ").strip().upper()
        if unit == "C":
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == "F":
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            print("Invalid input. Please specify 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print(f"Invalid unit entered. Please enter a numeric value.")
        
    
if __name__ == "__main__":
    main()
