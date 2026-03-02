This program is a temperature conversion tool.
It allows the user to convert temperatures between:

Celsius

Fahrenheit

Kelvin

It demonstrates functions, conditionals, user input, and basic formulas.

🔎 Line-by-Line Explanation
🔹 Part 1: The Function
1️⃣ Function Definition
def temp_converter(value, scale):

This defines a function named temp_converter.

It takes two parameters:

value → the temperature number

scale → the type of conversion (like "CtoF")

2️⃣ Celsius to Fahrenheit
if scale == "CtoF":
    return (value * 9/5) + 32

Formula used:

°
𝐹
=
(
°
𝐶
×
9
/
5
)
+
32
°F=(°C×9/5)+32

Example:

0°C → 32°F
3️⃣ Fahrenheit to Celsius
elif scale == "FtoC":
    return (value - 32) * 5/9

Formula used:

°
𝐶
=
(
°
𝐹
−
32
)
×
5
/
9
°C=(°F−32)×5/9

Example:

212°F → 100°C
4️⃣ Celsius to Kelvin
elif scale == "CtoK":
    return value + 273.15

Formula used:

𝐾
=
°
𝐶
+
273.15
K=°C+273.15

Example:

0°C → 273.15 K
5️⃣ Kelvin to Celsius
elif scale == "KtoC":
    return value - 273.15

Formula used:

°
𝐶
=
𝐾
−
273.15
°C=K−273.15
6️⃣ Invalid Scale Handling
else:
    return "Invalid scale. Use 'CtoF', 'FtoC', 'CtoK', or 'KtoC'."

If the user provides an incorrect scale, the function returns an error message.

🔹 Part 2: Main Program
7️⃣ Run Only If File Is Executed Directly
if __name__ == "__main__":

This ensures the program runs only when executed directly — not when imported into another file.

8️⃣ Display Menu
print("Conversion Options:")
print("1. Celsius to Fahrenheit (CtoF)")
print("2. Fahrenheit to Celsius (FtoC)")
print("3. Celsius to Kelvin (CtoK)")
print("4. Kelvin to Celsius (KtoC)")

Shows available options to the user.

9️⃣ Get User Input
choice = input("Enter your choice (CtoF, FtoC, CtoK, KtoC): ")
value = float(input("Enter the temperature value to convert: "))

choice → conversion type

value → numeric temperature (converted to float)

⚠️ Note:

The prompt asks for:

CtoF, FtoC, CtoK, KtoC

But the next code checks for:

"1", "2", "3", "4"

That means the user must type 1, not "CtoF".

There is a small mismatch between prompt and logic.

🔟 Set Conversion Scale
if choice == "1":
    scale = "CtoF"
    target = "Fahrenheit"

This converts numeric menu choice into:

scale → passed to the function

target → used for display

The same logic applies for other options.

1️⃣1️⃣ Invalid Choice
else:
    print("Invalid choice.")
    exit()

Stops the program if the input is wrong.

1️⃣2️⃣ Display Result
print(f"Converted Temperature: {temp_converter(value, scale):.2f} {target}")

This:

Calls the function

Formats the result to 2 decimal places

Displays the converted value with unit

Example output:

Converted Temperature: 98.60 Fahrenheit
🧠 What the Program Does Conceptually

Shows menu

Gets user choice

Converts choice into a scale code

Calls a function with proper formula

Displays formatted result

📚 Concepts Demonstrated

This program teaches:

1️⃣ Functions

Encapsulating logic inside reusable code.

2️⃣ Conditional Statements

Using if / elif / else.

3️⃣ User Input

Using input().

4️⃣ Mathematical Formulas

Implementing real-world equations.

5️⃣ String Formatting

Using :.2f for rounding.

💡 Practical Applications

This simple logic is used in:

🌡️ Weather Applications

Temperature conversion between:

Countries using Celsius

Countries using Fahrenheit

🧪 Scientific Software

Converting between:

Kelvin (used in physics)

Celsius (everyday use)

🏭 Engineering Systems

Industrial equipment may use:

Kelvin internally

Celsius for display

📱 Mobile Apps

Unit converters in:

Travel apps

Fitness trackers

Weather apps

📌 Summary

Your program:

Defines a reusable temperature conversion function

Uses correct scientific formulas

Handles user input

Displays formatted output

Demonstrates structured program design
