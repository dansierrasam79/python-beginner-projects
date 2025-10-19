def convert_temperature(value, unit):
    if unit == "C":
        # Celsius to Fahrenheit
        return (value * 9/5) + 32, "Fahrenheit"
    elif unit == "F":
        # Fahrenheit to Celsius
        return (value - 32) * 5/9, "Celsius"
    else:
        return None, None

try:
    # Ask user for the temperature value
    temp_input = input("Enter the temperature value: ")
    temperature = float(temp_input)  # Validate numeric input

    # Ask user for the unit
    unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Validate unit
    if unit not in ("C", "F"):
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    else:
        converted_value, converted_unit = convert_temperature(temperature, unit)
        print(f"Converted temperature: {converted_value:.2f}°{converted_unit[0]}")
except ValueError:
    print("Invalid input. Please enter a numeric temperature value.")
