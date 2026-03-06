This Python code demonstrates advanced formatting using f-strings.
It shows how to control decimal places, separators, percentages, alignment, width, and number systems when printing values.

These techniques are widely used in data reports, financial programs, logs, dashboards, and formatted outputs.

Below is a line-by-line explanation and practical application.

🔹 Part 1: Printing a Variable with f-Strings
pi = 3.14159

Creates a variable pi.

Stores the approximate value of π (pi).

print(f"pi = {pi}")

f"" means formatted string (f-string).

{pi} inserts the variable value.

Output:

pi = 3.14159
print(f"{pi = }")

{variable = } automatically prints the variable name and value.

Output:

pi = 3.14159

📌 Useful for debugging.

🔹 Part 2: Formatting Numbers
n = 1234567.89123

Stores a large decimal number.

Show 2 Decimal Places
print(f"{n = :.2f}")

.2f → show 2 decimal places

Output

n = 1234567.89

📌 Used in financial values and currency.

No Decimal Places
print(f"{n = :.0f}")

.0f → remove decimals.

Output

n = 1234568

📌 Used when rounding numbers.

Comma Separator
print(f"{n = :,.2f}")

, adds thousands separators.

Output

n = 1,234,567.89

📌 Used in:

Accounting

Sales reports

Financial dashboards

Underscore Separator
print(f"{n = :_.2f}")

_ separates thousands with underscores.

Output

n = 1_234_567.89

📌 Used in programming-friendly formats.

Scientific Notation
print(f"{n = :.2e}")

.2e converts number to scientific notation.

Output

n = 1.23e+06

📌 Used in:

Scientific computing

Physics calculations

Data science

Show Sign
print(f"{n = :+,.2f}")

+ forces showing + or − sign.

Output

n = +1,234,567.89

📌 Used in:

Profit/loss reports

Financial systems

🔹 Part 3: Percentage Formatting
progress = 0.4333

Represents 43.33% progress.

Percentage with 2 decimals
print(f"{progress = :.2%}")

Output

progress = 43.33%
Whole percentage
print(f"{progress = :.0%}")

Output

progress = 43%

📌 Used in:

Progress bars

Completion tracking

Statistics

🔹 Part 4: Dynamic Width and Precision
width = 10
dec = 3

Sets width and decimal precision dynamically.

print(f"{pi = :{width}.{dec}f}")

This means:

width = 10 characters

decimals = 3

Output:

pi =      3.142

📌 Used in:

Tables

Data alignment

Reports

🔹 Part 5: Text Alignment
text = "Pls follow"

Stores text string.

Left Alignment
print(f"{text = :<30}")

< aligns text left

total width = 30 characters.

Right Alignment with Dash
print(f"{text = :->30}")

> aligns right

fills empty space with -.

Center Alignment
print(f"{text = :*^30}")

^ centers text

* fills surrounding space.

Example output

text = ********Pls follow********

📌 Used in:

Console UI

CLI dashboards

Decorative formatting

🔹 Part 6: Number System Conversion
n = 255

Stores decimal value.

Binary
print(f"{n = :b}")

Output

n = 11111111

📌 Used in computer architecture and networking.

Octal
print(f"{n = :o}")

Output

n = 377
Hexadecimal (lowercase)
print(f"{n = :x}")

Output

n = ff
Hexadecimal (uppercase)
print(f"{n = :X}")

Output

n = FF
Hex with Prefix
print(f"{n = :#x}")

Output

n = 0xff

📌 Used in:

Memory addresses

Color codes (#FF0000)

Networking protocols

🧠 Overall Function of the Code

This program demonstrates how to:

Format numbers

Control decimal precision

Add separators

Display percentages

Align text

Convert number systems

Dynamically format output

All using Python f-strings.

🌍 Practical Applications
📊 1. Data Reports

Used when printing tables.

Example:

Revenue: $1,234,567.89
Growth: 43.3%
💰 2. Financial Software

Banks and accounting systems use:

+1,250.50
-450.25
🧪 3. Scientific Programs

Scientific notation:

1.23e+08

Used in physics, chemistry, and data science.

🖥️ 4. Command Line Tools

CLI tools use alignment formatting to display clean tables.

Example:

User        Score
John        95
Maria       87
🌐 5. Networking and Cybersecurity

Binary and hex formatting are used for:

IP calculations

Packet analysis

Memory debugging

⭐ Simple Summary

This code teaches how to format numbers and text cleanly in Python output, which is essential for:

Reports

Dashboards

Financial calculations

Scientific programs

System tools
