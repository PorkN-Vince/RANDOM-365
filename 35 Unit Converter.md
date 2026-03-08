This Python program is a Unit Converter. It allows a user to convert length, weight, or temperature values between different units through the terminal.

I’ll explain the function of the code, line by line, and then its practical applications.

1. Length Conversion Function
def convert_length(value, from_unit, to_unit):

Defines a function named convert_length.

It takes three parameters:

value → the number to convert

from_unit → the unit you are converting from

to_unit → the unit you want to convert to

length_units = {
    'meters': 1,
    'kilometers': 1000,
    'miles': 1609.34,
    'feet': 0.3048
}

A dictionary storing conversion values relative to meters.

Example:

1 kilometer = 1000 meters

1 mile = 1609.34 meters

This means meters are used as the base unit.

if from_unit not in length_units or to_unit not in length_units:
    raise ValueError("Unsupported length unit.")

Checks if the units entered by the user exist in the dictionary.

If not, Python raises an error to stop the program.

return value * length_units[from_unit] / length_units[to_unit]

This performs the conversion.

Steps:

Convert the value to meters

Convert meters to the target unit

Example:

Convert 1 mile → kilometers

1 × 1609.34 / 1000 = 1.609 km
2. Weight Conversion Function
def convert_weight(value, from_unit, to_unit):

Defines another function for weight conversion.

weight_units = {
    'grams': 1,
    'kilograms': 1000,
    'pounds': 453.592
}

Dictionary of weight units relative to grams.

Examples:

1 kilogram = 1000 grams

1 pound = 453.592 grams

if from_unit not in weight_units or to_unit not in weight_units:
    raise ValueError("Unsupported length unit.")

Checks if the entered units exist.

⚠ Minor mistake in your code:
The message says length unit but should say weight unit.

return value * weight_units[from_unit] / weight_units[to_unit]

Converts the weight using grams as the base unit.

Example:

2 kg → pounds
2 × 1000 / 453.592 = 4.41 lbs
3. Temperature Conversion Function
def convert_temperature(value, from_unit, to_unit):

Defines a function for temperature conversion.

Temperature is different because it does not use simple multiplication like length and weight.

if from_unit == to_unit:
    return value

If the units are the same, return the original value.

Example:

25°C → 25°C
Celsius Conversions
if from_unit == 'celsius':

If the input temperature is Celsius.

return(value *9/5) +32

Formula:

°F = (°C × 9/5) + 32

Example:

25°C → 77°F
return value + 273.15

Formula:

K = °C + 273.15
Fahrenheit Conversions
elif from_unit == 'fahrenheit':

If the starting unit is Fahrenheit.

return(value -32) * 9/5

⚠ Small mistake here.

Correct formula should be:

(value - 32) * 5/9
return (value -32) * 5/9 + 273.15

Converts Fahrenheit → Kelvin.

Kelvin Conversions
elif from_unit == 'kelvin':

If the unit is Kelvin.

return value - 273.15

Kelvin → Celsius.

return (value - 273.15) * 9/5 + 32

Kelvin → Fahrenheit.

raise ValueError("Unsupported Temperature unit.")

If the user inputs an unknown temperature unit, an error is raised.

4. Main Program
def main():

Defines the main function that runs the program.

print("Unit Converter")
print("1. Length")
print("2. Weight")
print("3. Temperature")

Displays a menu to the user.

choice = input("Choose the type fo convertion (1/2/3): ")

User selects the conversion type.

5. Length Conversion Section
if choice == '1':

If the user selects Length.

value = float(input("Enter value: "))

Gets the number to convert.

from_unit = input(...).lower()
to_unit = input(...).lower()

Gets the units and converts them to lowercase to prevent errors.

Example:

Meters → meters
result = convert_length(value, from_unit, to_unit)

Calls the length conversion function.

print(f"{value} {from_unit} is {result} {to_unit}")

Displays the result.

Example output:

5 miles is 8.0467 kilometers
6. Weight Conversion Section
elif choice == '2':

Runs if the user selects Weight.

result = convert_weight(value ,from_unit, to_unit)

Calls the weight conversion function.

7. Temperature Conversion Section
elif choice == '3':

Runs if the user selects Temperature.

result = convert_temperature(value, from_unit, to_unit)

Calls the temperature conversion function.

8. Invalid Choice
else:
    print("Invald choice.")

If the user enters anything other than 1, 2, or 3.

9. Program Entry Point
if __name__ == "__main__":
    main()

This ensures the program runs only when the file is executed directly.

Practical Applications

This program is a basic CLI (Command Line Interface) converter.

Real-world uses include:

1️⃣ Science and Engineering

Converting units in experiments.

Example:

meters → miles
2️⃣ Travel

Distance conversion.

Example:

10 miles → kilometers
3️⃣ Cooking

Weight conversion.

Example:

500 grams → pounds
4️⃣ Weather and Physics

Temperature conversion.

Example:

25°C → °F
5️⃣ Programming Practice

This project teaches:

Functions

Dictionaries

Conditional logic

User input

Error handling

These are core Python fundamentals.

Small Errors in Your Code
1️⃣ Fahrenheit → Celsius formula

Should be:

(value - 32) * 5/9

Not:

(value -32) * 9/5
2️⃣ Typo in prompt
fahrentheit

Should be:

fahrenheit
3️⃣ Error message
Unsupported length unit.

Should say:

Unsupported weight unit.
