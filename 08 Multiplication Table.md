This program generates a multiplication table for a number entered by the user. It demonstrates how to use functions, loops, user input, and formatted output in Python.

The Code
#Multiplication Table Program

#Multiplication Table Function
def multiplication_table(number):

    #Loop from 1 to 10
    for i in range(1, 11):

        #print table line
        print(f"{number} x {i} = {number * i}")
              
              
#Ask user for a number
num = int(input("Enter a number to see its multiplication table: "))
multiplication_table(num)
Line-by-Line Explanation
1️⃣ Comment (Program description)
#Multiplication Table Program

This is a comment that explains what the program does.
Comments are ignored by Python and are used only for documentation.

2️⃣ Comment (Function description)
#Multiplication Table Function

This comment explains that the next part of the code defines a function.

3️⃣ Function Definition
def multiplication_table(number):

This creates a function named:

multiplication_table

Purpose of the function:

Take a number as input

Print its multiplication table from 1 to 10

The variable number is a parameter, meaning it receives a value when the function is called.

Example:

multiplication_table(5)
4️⃣ Loop from 1 to 10
for i in range(1, 11):

This creates a loop.

range(1, 11)

Produces numbers:

1 2 3 4 5 6 7 8 9 10

The variable i represents the current multiplier.

So the function will calculate:

number × 1
number × 2
number × 3
...
number × 10
5️⃣ Print each line of the table
print(f"{number} x {i} = {number * i}")

This prints one line of the multiplication table.

f"" (f-string)

An f-string lets you insert variables inside a string.

Example:

number = 5
i = 3

This becomes:

5 x 3 = 15

Breakdown:

Part	Meaning
{number}	the chosen number
{i}	the multiplier
{number * i}	the product
6️⃣ Ask the User for Input
num = int(input("Enter a number to see its multiplication table: "))

This line does several things.

input()

Prompts the user to type something.

Example user input:

7

But input always returns text, not a number.

So we convert it.

int()

Converts the input string into an integer.

Example:

"7" → 7

This is necessary for multiplication.

The value is stored in:

num
7️⃣ Call the Function
multiplication_table(num)

This runs the function and sends the user's number into it.

Example:

num = 7

Function call becomes:

multiplication_table(7)
Example Program Run

User input:

Enter a number to see its multiplication table: 5

Output:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
Concepts Demonstrated

This small program teaches several important programming ideas.

Functions

Reusable blocks of code.

Loops

Repeating a process multiple times.

Variables

Storing and using values.

User Input

Getting data from the user.

String Formatting

Displaying dynamic values inside text.

Practical Applications

Even though this is a beginner program, the concepts are used in real software.

1️⃣ Educational Software

Apps that teach math generate tables like this dynamically.

Examples:

math learning apps

quiz programs

online tutors

2️⃣ Calculators

Basic calculators perform repeated arithmetic operations using loops.

3️⃣ Data Processing

Programs often apply the same calculation to multiple values.

Example:

price × quantity
tax × salary
score × weight

Loops automate this.

4️⃣ Report Generation

Systems automatically generate tables and summaries using loops.

Example:

Employee salary breakdown
Sales reports
Performance metrics
5️⃣ Automation Scripts

Developers often write scripts that apply formulas repeatedly to datasets.

Example:

convert currency
calculate interest
compute statistics
Why Functions Matter Here

Instead of writing this repeatedly:

print(5 x 1)
print(5 x 2)
...

We create a function that can be reused for any number.

Example calls:

multiplication_table(3)
multiplication_table(9)
multiplication_table(12)
Improved Version (Optional)

You can allow the user to generate multiple tables.

while True:
    num = int(input("Enter number (0 to exit): "))
    if num == 0:
        break
    multiplication_table(num)

This turns the program into a mini multiplication tool.
